# File: test_calc.py

import pytest
from unittest.mock import patch
from calc import calculator
from utils.operations import add, subtract, multiply, divide, power

@pytest.fixture(scope="module")
def mock_inputs():
    """Fixture to patch input calls."""
    with patch('builtins.input') as mocked_input:
        yield mocked_input

@pytest.fixture(scope="module")
def mock_print():
    """Fixture to patch print calls."""
    with patch('builtins.print') as mocked_print:
        yield mocked_print

def test_calculator_addition_normal_case(mock_inputs, mock_print):
    """Test calculator addition with normal inputs."""
    mock_inputs.side_effect = ['1', '5', '3']  # Choice 1 for add, then two numbers
    calculator()
    mock_print.assert_any_call("Result:", add(5, 3))

def test_calculator_subtraction_normal_case(mock_inputs, mock_print):
    """Test calculator subtraction with normal inputs."""
    mock_inputs.side_effect = ['2', '10', '3']
    calculator()
    mock_print.assert_any_call("Result:", subtract(10, 3))

def test_calculator_multiplication_normal_case(mock_inputs, mock_print):
    """Test calculator multiplication with normal inputs."""
    mock_inputs.side_effect = ['3', '4', '5']
    calculator()
    mock_print.assert_any_call("Result:", multiply(4, 5))

def test_calculator_division_normal_case(mock_inputs, mock_print):
    """Test calculator division with normal inputs."""
    mock_inputs.side_effect = ['4', '20', '5']
    calculator()
    mock_print.assert_any_call("Result:", divide(20, 5))

def test_calculator_division_by_zero(mock_inputs, mock_print):
    """Test calculator division by zero."""
    mock_inputs.side_effect = ['4', '20', '0']
    calculator()
    mock_print.assert_any_call("Result:", "Cannot divide by zero")

def test_calculator_power_normal_case(mock_inputs, mock_print):
    """Test calculator power function with normal inputs."""
    mock_inputs.side_effect = ['5', '2', '3']
    calculator()
    mock_print.assert_any_call("Result:", power(2, 3))

def test_calculator_invalid_choice(mock_inputs, mock_print):
    """Test calculator with invalid operation choice."""
    mock_inputs.side_effect = ['6']  # Invalid choice
    calculator()
    mock_print.assert_any_call("Invalid choice. Please select a valid option.")

def test_calculator_invalid_number_input(mock_inputs, mock_print):
    """Test calculator with invalid number input."""
    mock_inputs.side_effect = ['1', 'a', '3']  # Invalid number
    calculator()
    mock_print.assert_any_call("Invalid input. Please enter numbers only.")

@pytest.mark.parametrize("choice, num1, num2, result", [
    ('1', '10', '5', add(10, 5)),
    ('2', '10', '5', subtract(10, 5)),
    ('3', '10', '5', multiply(10, 5)),
    ('4', '10', '2', divide(10, 2)),
    ('5', '2', '3', power(2, 3)),
])
def test_calculator_operation_parametrized(mock_inputs, mock_print, choice, num1, num2, result):
    """Parametrized test for all operations with normal cases."""
    mock_inputs.side_effect = [choice, num1, num2]
    calculator()
    mock_print.assert_any_call("Result:", result)