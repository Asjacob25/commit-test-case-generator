import requests
import os
import sys
import logging
import json
from pathlib import Path
from requests.exceptions import RequestException
from typing import List, Optional, Dict, Any

# Set up logging
logging.basicConfig(
   level=logging.INFO,
   format='%(asctime)s - %(levelname)s - %(message)s'
)

class TestGenerator:
   def __init__(self):
       self.api_key = os.getenv('OPENAI_API_KEY')
       self.model = os.getenv('OPENAI_MODEL', 'gpt-4-turbo-preview')
       
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
           '.cpp':'C++',
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

   def get_related_files(self, file_name: str) -> List[str]:
        """Identify related files based on import statements or includes."""
        related_files = []
        try:
            with open(file_name, 'r') as f:
                for line in f:
                    # Example: Detecting imports in Python and JavaScript/TypeScript
                    if 'import ' in line or 'from ' in line or 'require(' in line:
                        parts = line.split()
                        for part in parts:
                            # Check for file extensions
                            if part.endswith(('.py', '.js', '.ts', '.java', '.cpp', '.cs')):
                                # Use Path to construct a relative path
                                related_path = Path(part)
                                if related_path.is_file():  # Check if the file exists in the same directory
                                    related_files.append(str(related_path))
                                else:
                                    # If not found, check in the project root or other common directories
                                    for ext in ('.py', '.js', '.ts', '.java', '.cpp', '.cs'):
                                        potential_file = related_path.with_suffix(ext)
                                        # Check for different directory structure
                                        for root, dirs, files in os.walk(Path('.')):
                                            if potential_file.name in files:
                                                related_files.append(os.path.join(root, potential_file.name))
                                                break  # Stop searching after finding the first match

                            # Check for class/module names without extensions
                            elif part.isidentifier():  # Checks if part is a valid identifier
                                # Construct potential file names
                                base_name = part.lower()  # Assuming file names are in lowercase
                                for ext in ('.py', '.js', '.ts', '.java', '.cpp', '.cs'):
                                    potential_file = f"{base_name}{ext}"
                                    # Search in the project root or other common directories
                                    for root, dirs, files in os.walk(Path('.')):
                                        if potential_file in files:
                                            related_files.append(os.path.join(root, potential_file))
                                            break  # Stop searching after finding the first match

        except Exception as e:
            logging.error(f"Error identifying related files in {file_name}: {e}")

        return list(set(related_files))  # Remove duplicates



   def create_prompt(self, file_name: str, language: str) -> Optional[str]:
        """Create a language-specific prompt for test generation."""
        try:
            with open(file_name, 'r') as f:
                code_content = f.read()
        except Exception as e:
            logging.error(f"Error reading file {file_name}: {e}")
            return None

        # Gather additional context from related files
        related_files = self.get_related_files(file_name)
        related_content = ""
        
        # Log related files to confirm detection
        if related_files:
            logging.info(f"Related files for {file_name}: {related_files}")
        else:
            logging.info(f"No related files found for {file_name}")
        
        for related_file in related_files:
            try:
                with open(related_file, 'r') as rf:
                    file_content = rf.read()
                    related_content += f"\n\n// Related file: {related_file}\n{file_content}"
                    logging.info(f"Included content from related file: {related_file}")
            except Exception as e:
                logging.error(f"Error reading related file {related_file}: {e}")

        framework = self.get_test_framework(language)
        
        prompt = f"""Generate comprehensive unit tests for the following {language} code using {framework}.

        Requirements:
        1. Include edge cases, normal cases, and error cases
        2. Use mocking where appropriate for external dependencies
        3. Include setup and teardown if needed
        4. Add descriptive test names and docstrings
        5. Follow {framework} best practices
        6. Ensure high code coverage
        7. Test both success and failure scenarios

        Code to test:

        {code_content}

        Related context:

        {related_content}

        Generate only the test code without any explanations or notes."""

        # Log the length of the final prompt to verify related content inclusion
        logging.info(f"Created prompt for {file_name} with length {len(prompt)} characters")
        return prompt

   def call_openai_api(self, prompt: str) -> Optional[str]:
       """Call OpenAI API to generate test cases."""
       headers = {
           'Content-Type': 'application/json',
           'Authorization': f'Bearer {self.api_key}'
       }
       
       data = {
           'model': self.model,
           'messages': [
               {
                   "role": "system",
                   "content": "You are a senior software engineer specialized in writing comprehensive test suites."
               },
               {
                   "role": "user",
                   "content": prompt
               }
           ],
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
           normalized_text = generated_text.replace('“', '"').replace('”', '"').replace("‘", "'").replace("’", "'")
           if normalized_text.startswith('```'):
               first_newline_index = normalized_text.find('\n', 3)
               if first_newline_index != -1:
                   normalized_text = normalized_text[first_newline_index+1:]
               else:
                   normalized_text = normalized_text[3:]
               if normalized_text.endswith('```'):
                   normalized_text = normalized_text[:-3]
           return normalized_text.strip()
       except RequestException as e:
           logging.error(f"API request failed: {e}")
           return None

   def save_test_cases(self, file_name: str, test_cases: str, language: str):
       """Save generated test cases to appropriate directory structure."""
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

       if test_file.exists():
           logging.info(f"File {test_file} exists with size {test_file.stat().st_size} bytes.")
       else:
           logging.error(f"File {test_file} was not created.")

   def run(self):
       """Main execution method."""
       changed_files = self.get_changed_files()
       if not changed_files:
           logging.info("No files changed.")
           return

       for file_name in changed_files:
           try:
               language = self.detect_language(file_name)
               if language == 'Unknown':
                   logging.warning(f"Unsupported file type: {file_name}")
                   continue

               logging.info(f"Processing {file_name} ({language})")
               prompt = self.create_prompt(file_name, language)
               
               if prompt:
                   test_cases = self.call_openai_api(prompt)
                   
                   if test_cases:
                       test_cases = test_cases.replace("“", '"').replace("”", '"')
                       self.save_test_cases(file_name, test_cases, language)
                   else:
                       logging.error(f"Failed to generate test cases for {file_name}")
           except Exception as e:
               logging.error(f"Error processing {file_name}: {e}")

if __name__ == '__main__':
   try:
       generator = TestGenerator()
       generator.run()
   except Exception as e:
       logging.error(f"Fatal error: {e}")
       sys.exit(1)
