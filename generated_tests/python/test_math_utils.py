import pytest
from unittest.mock import patch
from your_module import add, power, minusOne, subtract, multiply, divide, calculator

@pytest.fixture
def setup_and_teardown_function():
    # Setup if needed
    yield
    # Teardown if needed

def test_add_normal_cases():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_add_edge_cases():
    assert add(0, 0) == 0

def test_power_normal_cases():
    assert power(2, 3) == 8
    assert power(-1, 2) == 1

def test_power_edge_cases():
    assert power(2, 0) == 1

def test_minusOne_normal_cases():
    assert minusOne(10) == 9
    assert minusOne(-1) == -2

def test_minusOne_edge_cases():
    assert minusOne(0) == -1

def test_subtract_normal_cases():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0

def test_subtract_edge_cases():
    assert subtract(0, 0) == 0

def test_multiply_normal_cases():
    assert multiply(3, 4) == 12
    assert multiply(-1, 3) == -3

def test_multiply_edge_cases():
    assert multiply(0, 10) == 0

def test_divide_normal_cases():
    assert divide(10, 2) == 5
    assert divide(-4, 2) == -2

def test_divide_edge_cases():
    assert divide(0, 1) == 0

def test_divide_error_cases():
    assert divide(5, 0) == "Error: Division by zero!"

@patch('builtins.input', side_effect=['1', '5', '3', 'exit'])
@patch('builtins.print')
def test_calculator_addition(mock_print, mock_input):
    calculator()
    mock_print.assert_called_with('5.0 + 3.0 = 8.0')

@patch('builtins.input', side_effect=['2', '5', '3', 'exit'])
@patch('builtins.print')
def test_calculator_subtraction(mock_print, mock_input):
    calculator()
    mock_print.assert_called_with('5.0 - 3.0 = 2.0')

@patch('builtins.input', side_effect=['3', '5', '3', 'exit'])
@patch('builtins.print')
def test_calculator_multiplication(mock_print, mock_input):
    calculator()
    mock_print.assert_called_with('5.0 * 3.0 = 15.0')

@patch('builtins.input', side_effect=['4', '6', '3', 'exit'])
@patch('builtins.print')
def test_calculator_division(mock_print, mock_input):
    calculator()
    mock_print.assert_called_with('6.0 / 3.0 = 2.0')

@patch('builtins.input', side_effect=['4', '5', '0', 'exit'])
@patch('builtins.print')
def test_calculator_division_by_zero(mock_print, mock_input):
    calculator()
    mock_print.assert_called_with('5.0 / 0.0 = Error: Division by zero!')

@patch('builtins.input', side_effect=['exit'])
@patch('builtins.print')
def test_calculator_exit(mock_print, mock_input):
    calculator()
    mock_print.assert_called_with("Exiting the calculator. Goodbye!")

@patch('builtins.input', side_effect=['5', 'exit'])  # Invalid choice
@patch('builtins.print')
def test_calculator_invalid_input(mock_print, mock_input):
    calculator()
    mock_print.assert_called_with("Invalid input. Please enter a number from 1 to 4.")