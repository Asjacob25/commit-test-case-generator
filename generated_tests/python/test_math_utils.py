# Import necessary modules and functions
import pytest
from your_module import add, power, subtract, multiply, divide, calculator
from unittest.mock import patch, MagicMock

# Add function tests
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 0, 0),
    (float('inf'), 1, float('inf')),  # Edge case
    (1, float('inf'), float('inf')),  # Edge case
])
def test_add(a, b, expected):
    """Test the add function with various inputs."""
    assert add(a, b) == expected

# Power function tests
@pytest.mark.parametrize("base, exponent, expected", [
    (2, 3, 8),
    (2, 0, 1),
    (2, -1, 0.5),
    (2, float('inf'), float('inf')),  # Edge case
    (2, -float('inf'), 0),  # Edge case
])
def test_power(base, exponent, expected):
    """Test the power function with various inputs."""
    assert power(base, exponent) == expected

# Subtract function tests
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (-1, -2, 1),
    (0, 0, 0),
    (-float('inf'), 1, -float('inf')),  # Edge case
    (1, -float('inf'), float('inf')),  # Edge case
])
def test_subtract(a, b, expected):
    """Test the subtract function with various inputs."""
    assert subtract(a, b) == expected

# Multiply function tests
@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (5, 0, 0),
    (-3, 4, -12),
    (float('inf'), 1, float('inf')),  # Edge case
    (1, float('inf'), float('inf')),  # Edge case
])
def test_multiply(a, b, expected):
    """Test the multiply function with various inputs."""
    assert multiply(a, b) == expected

# Divide function tests
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (-6, 3, -2),
    (6, -3, -2),
    (0, 1, 0),  # Edge case: zero divided by anything
])
def test_divide(a, b, expected):
    """Test the divide function with various inputs, except division by zero."""
    assert divide(a, b) == expected

def test_divide_by_zero():
    """Test division by zero, should return an error message."""
    assert divide(5, 0) == "Error: Division by zero!"

# Mock tests for calculator UI interactions
@patch('builtins.input')
@patch('builtins.print')
def test_calculator_exit(mock_print, mock_input):
    """Test exiting the calculator."""
    mock_input.side_effect = ['exit']
    with pytest.raises(SystemExit):
        calculator()
    mock_print.assert_called_with("Exiting the calculator. Goodbye!")

@patch('builtins.input')
@patch('builtins.print')
def test_calculator_addition(mock_print, mock_input):
    """Test calculator addition operation."""
    mock_input.side_effect = ['1', '5', '3', 'exit']
    calculator()
    mock_print.assert_any_call("5.0 + 3.0 = 8.0")

@patch('builtins.input')
@patch('builtins.print')
def test_calculator_invalid_input(mock_print, mock_input):
    """Test handling of invalid input in the calculator."""
    mock_input.side_effect = ['5', 'exit']  # 5 is an invalid choice
    calculator()
    mock_print.assert_any_call("Invalid input. Please enter a number from 1 to 4.")