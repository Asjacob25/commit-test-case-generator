import pytest
from unittest.mock import patch
from utils.operations import add, subtract, multiply, divide, power

# Test cases for operations in utils/operations.py

@pytest.mark.parametrize("x, y, expected", [
    (5, 3, 8),
    (-1, -1, -2),
    (0, 0, 0),
])
def test_add(x, y, expected):
    assert add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (5, 3, 2),
    (-1, -1, 0),
    (0, 0, 0),
])
def test_subtract(x, y, expected):
    assert subtract(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (5, 3, 15),
    (-1, -1, 1),
    (0, 0, 0),
])
def test_multiply(x, y, expected):
    assert multiply(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (5, 3, 1.6666666666666667),
    (-1, -1, 1),
    (5, 0, "Cannot divide by zero"),
])
def test_divide(x, y, expected):
    assert divide(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 8),
    (-1, 2, 1),
    (5, 0, 1),
])
def test_power(x, y, expected):
    assert power(x, y) == expected

# Test cases for calculator function with mocking input and print

@pytest.fixture
def mock_input_output():
    with patch('builtins.input', side_effect=['1', '5', '3']), patch('builtins.print') as mock_print:
        yield mock_print

def test_calculator_addition(mock_input_output):
    from calculator import calculator
    calculator()
    mock_input_output.assert_called_with("Result:", 8)

@pytest.fixture
def mock_invalid_choice():
    with patch('builtins.input', side_effect=['6']), patch('builtins.print') as mock_print:
        yield mock_print

def test_calculator_invalid_choice(mock_invalid_choice):
    from calculator import calculator
    calculator()
    mock_invalid_choice.assert_called_with("Invalid choice. Please select a valid option.")

@pytest.fixture
def mock_invalid_input():
    with patch('builtins.input', side_effect=['1', 'abc', '5']), patch('builtins.print') as mock_print:
        yield mock_print

def test_calculator_invalid_input(mock_invalid_input):
    from calculator import calculator
    calculator()
    mock_invalid_input.assert_called_with("Invalid input. Please enter numbers only.")

@pytest.fixture
def mock_divide_by_zero():
    with patch('builtins.input', side_effect=['4', '5', '0']), patch('builtins.print') as mock_print:
        yield mock_print

def test_calculator_divide_by_zero(mock_divide_by_zero):
    from calculator import calculator
    calculator()
    mock_divide_by_zero.assert_called_with("Result:", "Cannot divide by zero")