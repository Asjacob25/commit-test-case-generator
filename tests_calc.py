import pytest
from unittest.mock import patch
from calc import calculator
from utils.operations import add, subtract, multiply, divide, power

@pytest.fixture
def mock_add():
    """Fixture to mock the add function."""
    with patch('utils.operations.add', return_value=5) as _add:
        yield _add

@pytest.fixture
def mock_subtract():
    """Fixture to mock the subtract function."""
    with patch('utils.operations.subtract', return_value=-1) as _subtract:
        yield _subtract

@pytest.fixture
def mock_multiply():
    """Fixture to mock the multiply function."""
    with patch('utils.operations.multiply', return_value=6) as _multiply:
        yield _multiply

@pytest.fixture
def mock_divide():
    """Fixture to mock the divide function."""
    with patch('utils.operations.divide', return_value=2) as _divide:
        yield _divide

@pytest.fixture
def mock_power():
    """Fixture to mock the power function."""
    with patch('utils.operations.power', return_value=8) as _power:
        yield _power

@pytest.fixture
def mock_divide_by_zero():
    """Fixture to mock divide function for division by zero scenario."""
    with patch('utils.operations.divide', return_value="Cannot divide by zero") as _divide_zero:
        yield _divide_zero

def test_calculator_addition(mock_add):
    """Test calculator addition functionality."""
    with patch('builtins.input', side_effect=["1", "2", "3"]), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_called_with("Result:", 5)

def test_calculator_subtraction(mock_subtract):
    """Test calculator subtraction functionality."""
    with patch('builtins.input', side_effect=["2", "3", "4"]), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_called_with("Result:", -1)

def test_calculator_multiplication(mock_multiply):
    """Test calculator multiplication functionality."""
    with patch('builtins.input', side_effect=["3", "2", "3"]), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_called_with("Result:", 6)

def test_calculator_division(mock_divide):
    """Test calculator division functionality."""
    with patch('builtins.input', side_effect=["4", "4", "2"]), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_called_with("Result:", 2)

def test_calculator_power(mock_power):
    """Test calculator power functionality."""
    with patch('builtins.input', side_effect=["5", "2", "3"]), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_called_with("Result:", 8)

def test_calculator_divide_by_zero(mock_divide_by_zero):
    """Test calculator division by zero."""
    with patch('builtins.input', side_effect=["4", "4", "0"]), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_called_with("Result:", "Cannot divide by zero")

def test_calculator_invalid_option():
    """Test calculator with an invalid option."""
    with patch('builtins.input', side_effect=["6"]), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_called_with("Invalid choice. Please select a valid option.")

def test_calculator_invalid_number_input():
    """Test calculator with a non-numeric input for numbers."""
    with patch('builtins.input', side_effect=["1", "a", "b"]), patch('builtins.print') as mock_print:
        calculator()
        mock_print.assert_called_with("Invalid input. Please enter numbers only.")
