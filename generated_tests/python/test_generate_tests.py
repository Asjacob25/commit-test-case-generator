import pytest
from unittest.mock import patch, MagicMock
from requests.exceptions import RequestException
from your_module import TestGenerator

# Fixture for setting up environment variables
@pytest.fixture(autouse=True)
def setup_env_vars():
    with patch.dict("os.environ", {
        "OPENAI_API_KEY": "test_api_key",
        "OPENAI_MODEL": "test_model",
        "OPENAI_MAX_TOKENS": "100"
    }):
        yield

# Fixture for mocking file content
@pytest.fixture
def mock_file_content():
    with patch("builtins.open", mock_open(read_data="test code")) as mocked_file:
        yield mocked_file

# Test initialization and environment variable loading
def test_initialization_with_correct_env_vars():
    """Test initialization reads and sets environment variables correctly."""
    tg = TestGenerator()
    assert tg.api_key == "test_api_key"
    assert tg.model == "test_model"
    assert tg.max_tokens == 100

def test_initialization_fails_without_api_key():
    """Test initialization fails without API key."""
    with patch.dict("os.environ", {"OPENAI_API_KEY": ""}):
        with pytest.raises(ValueError):
            TestGenerator()

def test_initialization_fails_with_invalid_max_tokens():
    """Test initialization fails with invalid max tokens."""
    with patch.dict("os.environ", {"OPENAI_MAX_TOKENS": "not_a_number"}):
        with pytest.raises(SystemExit):
            TestGenerator()

# Test command line argument parsing
def test_get_changed_files(mock_sys_argv):
    """Test extraction of changed files from command line arguments."""
    tg = TestGenerator()
    assert tg.get_changed_files() == ["test_file.py", "test_file2.js"]

# Test language detection
@pytest.mark.parametrize("file, expected_language", [
    ("test.py", "Python"),
    ("test.js", "JavaScript"),
    ("unknown.ext", "Unknown")
])
def test_detect_language(file, expected_language):
    """Test language detection based on file extension."""
    tg = TestGenerator()
    assert tg.detect_language(file) == expected_language

# Test file reading error handling in create_prompt
def test_create_prompt_handles_file_read_error(mock_file_content):
    """Test create_prompt handles file read errors gracefully."""
    mock_file_content.side_effect = Exception("File read error")
    tg = TestGenerator()
    with patch("your_module.logging.error") as mock_log_error:
        assert tg.create_prompt("nonexistent_file.py", "Python") is None
        mock_log_error.assert_called_once()

# Test OpenAI API call success and failure
@patch("requests.post")
def test_call_openai_api_success(mock_post):
    """Test successful OpenAI API call."""
    mock_response = MagicMock()
    mock_response.json.return_value = {"choices": [{"message": {"content": "Test content"}}]}
    mock_post.return_value = mock_response

    tg = TestGenerator()
    result = tg.call_openai_api("Sample prompt")
    assert result == "Test content"

@patch("requests.post")
def test_call_openai_api_failure(mock_post):
    """Test failure of OpenAI API call."""
    mock_post.side_effect = RequestException("API request failed")

    tg = TestGenerator()
    with patch("your_module.logging.error") as mock_log_error:
        assert tg.call_openai_api("Sample prompt") is None
        mock_log_error.assert_called_once()

# Example of a test for save_test_cases method (assuming its implementation)
@patch("builtins.open", new_callable=mock_open)
def test_save_test_cases(mock_open):
    """Test saving test cases to a file."""
    tg = TestGenerator()
    tg.save_test_cases("test_file.py", "Test content")
    mock_open.assert_called_once_with("test_file_test_cases.py", "w")
    mock_open().write.assert_called_once_with("Test content")

# Example of a test for the run method (assuming its implementation and dependencies)
@patch("your_module.TestGenerator.call_openai_api")
@patch("your_module.TestGenerator.create_prompt")
@patch("your_module.TestGenerator.detect_language")
@patch("your_module.TestGenerator.get_changed_files")
def test_run(mock_get_changed_files, mock_detect_language, mock_create_prompt, mock_call_openai_api):
    """Test the run method processes files and interacts with the OpenAI API."""
    mock_get_changed_files.return_value = ["test_file.py"]
    mock_detect_language.return_value = "Python"
    mock_create_prompt.return_value = "Test prompt"
    mock_call_openai_api.return_value = "Test response"

    tg = TestGenerator()
    tg.run()

    mock_get_changed_files.assert_called_once()
    mock_detect_language.assert_called_once_with("test_file.py")
    mock_create_prompt.assert_called_once_with("test_file.py", "Python")
    mock_call_openai_api.assert_called_once_with("Test prompt")