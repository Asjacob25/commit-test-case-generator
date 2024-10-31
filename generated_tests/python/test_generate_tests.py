# test_test_generator.py
import json
import os
import pytest
from unittest.mock import patch, mock_open
from test_generator import TestGenerator, RequestException

# Constants for use in tests
VALID_FILE_PATH = "valid_code.py"
INVALID_FILE_PATH = "invalid_code.txt"
API_RESPONSE_SUCCESS = '{"choices": [{"message": {"content": "Test content"}}]}'
API_RESPONSE_FAILURE = '{"error": "Test error"}'

@pytest.fixture
def test_generator():
    """Fixture to create a TestGenerator instance."""
    return TestGenerator()

@pytest.fixture
def env_vars():
    """Fixture to set environment variables."""
    os.environ['OPENAI_API_KEY'] = 'testkey'
    os.environ['OPENAI_MODEL'] = 'gpt-4-turbo-preview'
    os.environ['OPENAI_MAX_TOKENS'] = '2000'
    yield
    os.environ.pop('OPENAI_API_KEY')
    os.environ.pop('OPENAI_MODEL')
    os.environ.pop('OPENAI_MAX_TOKENS')

def test_init_success(env_vars):
    """Test successful initialization of TestGenerator."""
    generator = TestGenerator()
    assert generator.api_key == 'testkey'
    assert generator.model == 'gpt-4-turbo-preview'
    assert generator.max_tokens == 2000

def test_init_failure_no_api_key():
    """Test failure of initialization when API key is not set."""
    with pytest.raises(ValueError) as e:
        TestGenerator()
    assert "OPENAI_API_KEY environment variable is not set" in str(e.value)

@patch('sys.argv', ['', VALID_FILE_PATH])
def test_get_changed_files_returns_correct_list(test_generator):
    """Test that changed files are correctly retrieved."""
    files = test_generator.get_changed_files()
    assert files == [VALID_FILE_PATH]

@patch('sys.argv', [''])
def test_get_changed_files_empty_when_no_args(test_generator):
    """Test that no files are returned when no arguments are passed."""
    assert test_generator.get_changed_files() == []

@pytest.mark.parametrize("file_name, expected_language", [
    ("file.py", "Python"),
    ("file.js", "JavaScript"),
    ("file.unknown", "Unknown"),
])
def test_detect_language_correct_detection(test_generator, file_name, expected_language):
    """Test correct detection of programming languages."""
    assert test_generator.detect_language(file_name) == expected_language

@pytest.mark.parametrize("language, expected_framework", [
    ("Python", "pytest"),
    ("Unknown", "unknown"),
])
def test_get_test_framework_correct_framework(test_generator, language, expected_framework):
    """Test retrieval of correct test framework based on language."""
    assert test_generator.get_test_framework(language) == expected_framework

@patch("builtins.open", new_callable=mock_open, read_data="code content")
def test_create_prompt_returns_correct_prompt(mock_file, test_generator):
    """Test creation of correct prompt for test generation."""
    prompt = test_generator.create_prompt(VALID_FILE_PATH, "Python")
    assert "Generate comprehensive unit tests for the following Python code using pytest." in prompt

@patch("builtins.open", mock_open(read_data="code content"), create=True)
@patch("test_generator.TestGenerator.get_test_framework", return_value="pytest")
def test_create_prompt_handles_file_error(mock_get_framework, test_generator):
    """Test handling of file read error in create_prompt."""
    with patch("builtins.open", side_effect=Exception("File read error")):
        prompt = test_generator.create_prompt(INVALID_FILE_PATH, "Python")
        assert prompt is None

@patch("requests.post")
def test_call_openai_api_success(mock_post, test_generator, env_vars):
    """Test successful API call to OpenAI."""
    mock_post.return_value.json.return_value = json.loads(API_RESPONSE_SUCCESS)
    mock_post.return_value.raise_for_status = lambda: None
    result = test_generator.call_openai_api("test prompt")
    assert "Test content" in result

@patch("requests.post")
def test_call_openai_api_failure(mock_post, test_generator, env_vars):
    """Test handling of failure in API call to OpenAI."""
    mock_post.side_effect = RequestException("API request failed")
    result = test_generator.call_openai_api("test prompt")
    assert result is None

@patch("builtins.open", mock_open(), create=True)
def test_save_test_cases_creates_file_correctly(test_generator):
    """Test that save_test_cases method creates a file with the correct content."""
    test_content = "Test case content"
    test_generator.save_test_cases(test_content, "test_output.py")
    mock_open().write.assert_called_once_with(test_content)

@patch("builtins.open", mock_open(), create=True)
def test_save_test_cases_file_error_handling(test_generator):
    """Test error handling in save_test_cases method."""
    with patch("builtins.open", side_effect=Exception("File write error")):
        with pytest.raises(Exception) as e:
            test_generator.save_test_cases("Test case content", "test_output.py")
        assert "File write error" in str(e.value)