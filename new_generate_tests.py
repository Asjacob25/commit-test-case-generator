import requests
import os
import sys
import logging
import json
import subprocess
from pathlib import Path
from requests.exceptions import RequestException
from typing import List, Optional

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TestGenerator:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = os.getenv('OPENAI_MODEL', 'gpt-4-turbo-preview')
        self.conversation = []  # Track the conversation for iterative feedback
        
        try:
            self.max_tokens = int(os.getenv('OPENAI_MAX_TOKENS', '2000'))
        except ValueError:
            logging.error("Invalid value for OPENAI_MAX_TOKENS. Using default value: 2000")
            self.max_tokens = 2000

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")

    def get_changed_files(self) -> List[str]:
        """Retrieve list of changed files passed as command-line arguments."""
        if len(sys.argv) <= 1:
            return []
        return [f.strip() for f in sys.argv[1].split() if f.strip()]

    def detect_language(self, file_name: str) -> str:
        """Detect programming language based on file extension."""
        extensions = {
            '.py': 'Python',
            '.js': 'JavaScript',
            '.ts': 'TypeScript',
            '.java': 'Java',
            '.cpp': 'C++',
            '.cs': 'C#'
        }
        _, ext = os.path.splitext(file_name)
        return extensions.get(ext.lower(), 'Unknown')

    def get_test_framework(self, language: str) -> str:
        """Get the appropriate test framework based on language."""
        frameworks = {
            'Python': 'pytest',
            'JavaScript': 'jest',
            'TypeScript': 'jest',
            'Java': 'JUnit',
            'C++': 'Google Test',
            'C#': 'NUnit'
        }
        return frameworks.get(language, 'unknown')

    def get_related_files(self, language: str, file_name: str) -> List[str]:
        """Identify related files based on import statements or includes."""
        related_files = []
        try:
            if language in {"Python", "JavaScript", "TypeScript"}:
                with open(file_name, 'r') as f:
                    for line in f:
                        # Detecting imports in Python and JavaScript/TypeScript
                        if 'import ' in line or 'from ' in line or 'require(' in line:
                            parts = line.split()
                            for part in parts:
                                # Check for file extensions
                                if '.' in part:
                                    path = part.replace(".", "/")
                                    for ext in ('.py', '.js', '.ts'):
                                        potential_file = f"{path}{ext}"
                                        if Path(potential_file).exists():
                                            related_files.append(potential_file)
                                            break
                                else:
                                    if part.endswith(('.py', '.js', '.ts')) and Path(part).exists():
                                        related_files.append(part)
                                    elif part.isidentifier():
                                        base_name = part.lower()
                                        for ext in ('.py', '.js', '.ts'):
                                            potential_file = f"{base_name}{ext}"
                                            if Path(potential_file).exists():
                                                related_files.append(potential_file)
                                                break
            elif language in {'C++', 'C#'}:
                return []  # Placeholder for future logic

        except Exception as e:
            logging.error(f"Error identifying related files in {file_name}: {e}")
        return related_files

    def create_prompt(self, file_name: str, language: str) -> Optional[str]:
        """Create a language-specific prompt for test generation."""
        try:
            with open(file_name, 'r') as f:
                code_content = f.read()
        except Exception as e:
            logging.error(f"Error reading file {file_name}: {e}")
            return None

        related_files = self.get_related_files(language, file_name)
        related_content = ""

        for related_file in related_files:
            try:
                with open(related_file, 'r') as rf:
                    file_content = rf.read()
                    module_path = str(Path(related_file).with_suffix('')).replace('/', '.')
                    import_statement = f"import {module_path}"
                    related_content += f"\n\n// Module: {module_path}\n{import_statement}\n{file_content}"
            except Exception as e:
                logging.error(f"Error reading related file {related_file}: {e}")

        framework = self.get_test_framework(language)
        prompt = f"""Generate comprehensive unit tests for the following {language} file: {file_name} using {framework}.

        Requirements:
        1. Include edge cases, normal cases, and error cases.
        2. Use mocking where appropriate for external dependencies.
        3. Include setup and teardown if needed.
        4. Add descriptive test names and docstrings.
        5. Follow {framework} best practices.
        6. Ensure high code coverage.
        7. Test both success and failure scenarios.

        Code to test (File: {file_name}):

        {code_content}

        Related context:

        {related_content}

        Generate only the test code without any explanations or notes."""

        logging.info(f"Created prompt for {file_name} with length {len(prompt)} characters")
        self.conversation.append({"role": "user", "content": prompt})  # Track the initial prompt
        return prompt

    def call_openai_api(self, prompt: str) -> Optional[str]:
        """Call OpenAI API to generate or refine test cases."""
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {self.api_key}'
        }
        
        data = {
            'model': self.model,
            'messages': self.conversation,  # Send the entire conversation context
            'max_tokens': self.max_tokens,
            'temperature': 0.7
        }

        try:
            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers=headers,
                json=data,
                timeout=60
            )
            response.raise_for_status()
            generated_text = response.json()['choices'][0]['message']['content']
            self.conversation.append({"role": "assistant", "content": generated_text})  # Track assistant response
            return generated_text.strip()
        except RequestException as e:
            logging.error(f"API request failed: {e}")
            return None

    def refine_test_cases(self, test_results: str):
        """Refine test cases based on test run results."""
        followup_prompt = f"Here are the test results:\n{test_results}. Please improve the test cases to cover any failed or missed scenarios."
        self.conversation.append({"role": "user", "content": followup_prompt})  # Add follow-up message to context
        refined_test_cases = self.call_openai_api(followup_prompt)
        return refined_test_cases
        #logging.info("got to refined test cases")
        #return "got to refined test cases"

    def save_test_cases(self, file_name: str, test_cases: str, language: str, initial: bool = False):
        """Save generated or refined test cases."""
        # Specify the file name for initial test cases without a directory
        if initial:
            # Determine the file extension based on the language
            extension = '.js' if language == 'JavaScript' else Path(file_name).suffix
            test_file = f"{Path(file_name).stem}_initial_tests{extension}"  # Use correct extension
        else:
            tests_dir = Path('generated_tests')
            tests_dir.mkdir(exist_ok=True)
            lang_dir = tests_dir / language.lower()
            lang_dir.mkdir(exist_ok=True)
            base_name = Path(file_name).stem
            if not base_name.startswith("test_"):
                base_name = f"test_{base_name}"
            extension = '.js' if language == 'JavaScript' else Path(file_name).suffix
            test_file = lang_dir / f"{base_name}{extension}"

        try:
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(test_cases)
            logging.info(f"Test cases saved to {test_file}")
        except Exception as e:
            logging.error(f"Error saving test cases to {test_file}: {e}")

    def run_tests(self, language: str, base_file_name: str) -> str:
        """Run the tests and capture the results."""
        # Determine the test file extension based on the programming language
        if language == 'Python':
            test_file = f"{base_file_name}.py"
            command = ['pytest', test_file, '--tb=short']
        elif language in ['JavaScript', 'TypeScript']:
            test_file = f"{base_file_name}.js"
            command = ['npm', 'test', '--', test_file]
        elif language == 'Java':
            test_file = f"{base_file_name}.java"  # Assuming you are using .java files for tests
            command = ['gradle', 'test']
        elif language == 'C++':
            test_file = f"{base_file_name}.cpp"
            compile_command = ['g++', '-o', 'test_runner', test_file]
            subprocess.run(compile_command, check=True)  # Compile the C++ file
            command = ['./test_runner']  # Run the compiled executable
        elif language == 'C#':
            test_file = f"{base_file_name}.cs"
            command = ['dotnet', 'test', test_file]
        else:
            logging.error(f"Unsupported language: {language}")
            return "No tests were run due to unsupported language."

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            logging.info("Tests executed successfully.")
            return result.stdout + "\n" + result.stderr
        except subprocess.CalledProcessError as e:
            # logging.error(f"Error running tests: {e}")
            # logging.error(f"Error running tests:\nstdout:\n{e.stdout}\nstderr:\n{e.stderr}")
            return f"Error running tests:\nstdout:\n{e.stdout}\nstderr:\n{e.stderr}"

    def install_test_package(self, language: str):
        """Install necessary test packages based on the language."""
        try:
            if language == 'Python':
                subprocess.run(['pip', 'install', 'pytest'], check=True)
                logging.info("installed pytest")
            elif language in ['JavaScript', 'TypeScript']:
                subprocess.run(['npm', 'install', '--save-dev', 'jest'], check=True)
            elif language == 'Java':
                subprocess.run(['gradle', 'add', 'test'], check=True)  # Adjust according to your build system
            elif language == 'C++':
                logging.info("Google Test should be included in your C++ project setup.")
            elif language == 'C#':
                subprocess.run(['dotnet', 'add', 'package', 'NUnit'], check=True)
            else:
                logging.warning(f"Unsupported language for package installation: {language}")
        except Exception as e:
            logging.error(f"Failed to install test package for {language}: {e}")

    def run(self):
        """Main execution method."""
        changed_files = self.get_changed_files()
        if not changed_files:
            logging.info("No files changed.")
            return

        for file_name in changed_files:
            if file_name != "new_generate_tests.py":
                try:
                    language = self.detect_language(file_name)
                    if language == 'Unknown':
                        logging.warning(f"Unsupported file type: {file_name}")
                        continue

                    logging.info(f"Processing {file_name} ({language})")
                    
                    # Install the necessary test package for the language
                    self.install_test_package(language)

                    prompt = self.create_prompt(file_name, language)
                    
                    if prompt:
                        initial_test_cases = self.call_openai_api(prompt)
                        logging.info(f"these are the initial test cases: {initial_test_cases}")
                        
                        if initial_test_cases:
                            # Save initial test cases outside the generated_tests directory
                            test_file_name = f"test_+{file_name}"
                            self.save_test_cases(test_file_name, initial_test_cases, language, initial=True)
                            
                            # Call run_tests with the base file name
                            base_file_name = Path(test_file_name).stem  # Get the base name without extension
                            test_results = self.run_tests(language, base_file_name)
                            logging.info(f"these are the test results: {test_results}")
                            
                            refined_test_cases = self.refine_test_cases(test_results)
                            logging.info(f"these are the refined tests: {refined_test_cases}")

                            
                            if refined_test_cases:
                                # Save refined test cases in the generated_tests directory
                                self.save_test_cases(file_name, refined_test_cases, language, initial=False)
                        else:
                            logging.error(f"Failed to generate test cases for {file_name}")
                except Exception as e:
                    logging.error(f"Error processing {file_name}: {e}")

if __name__ == "__main__":
    generator = TestGenerator()
    generator.run()
