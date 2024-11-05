# File: test_calc.py
import pytest
from unittest.mock import patch
import calc
from utils.operations import add, subtract, multiply, divide, power

@pytest.fixture
def mock_input():
    with patch('builtins.input') as mocked_input:
        yield mocked_input

@pytest.fixture
def mock_print(mocker):
    return mocker.patch('builtins.print')

def test_addition_normal_case(mock_input, mock_print):
    """
    Test normal case for addition
    """
    mock_input.side_effect = ['1', '5', '3']
    calc.calculator()
    mock_print.assert_called_with("Result:", add(5, 3))

def test_subtraction_normal_case(mock_input, mock_print):
    """
    Test normal case for subtraction
    """
    mock_input.side_effect = ['2', '10', '5']
    calc.calculator()
    mock_print.assert_called_with("Result:", subtract(10, 5))

def test_multiplication_normal_case(mock_input, mock_print):
    """
    Test normal case for multiplication
    """
    mock_input.side_effect = ['3', '4', '5']
    calc.calculator()
    mock_print.assert_called_with("Result:", multiply(4, 5))

def test_division_normal_case(mock_input, mock_print):
    """
    Test normal case for division
    """
    mock_input.side_effect = ['4', '20', '5']
    calc.calculator()
    mock_print.assert_called_with("Result:", divide(20, 5))

def test_division_by_zero_case(mock_input, mock_print):
    """
    Test division by zero
    """
    mock_input.side_effect = ['4', '5', '0']
    calc.calculator()
    mock_print.assert_called_with("Result:", "Cannot divide by zero")

def test_power_normal_case(mock_input, mock_print):
    """
    Test normal case for power
    """
    mock_input.side_effect = ['5', '2', '3']
    calc.calculator()
    mock_print.assert_called_with("Result:", power(2, 3))

def test_invalid_choice(mock_input, mock_print):
    """
    Test invalid choice
    """
    mock_input.side_effect = ['6']
    calc.calculator()
    mock_print.assert_called_with("Invalid choice. Please select a valid option.")

def test_invalid_number_input(mock_input, mock_print):
    """
    Test invalid number input
    """
    mock_input.side_effect = ['1', 'five', '3']
    calc.calculator()
    mock_print.assert_called_with("Invalid input. Please enter numbers only.")

@pytest.mark.parametrize("choice, num1, num2, result", [
    ('1', '10', '2', add(10, 2)),
    ('2', '10', '2', subtract(10, 2)),
    ('3', '10', '2', multiply(10, 2)),
    ('4', '10', '2', divide(10, 2)),
    ('4', '10', '0', "Cannot divide by zero"),
    ('5', '10', '2', power(10, 2)),
])
def test_calculator_operations(mock_input, mock_print, choice, num1, num2, result):
    """
    Test calculator operations with parametrized test cases
    """
    mock_input.side_effect = [choice, num1, num2]
    calc.calculator()
    mock_print.assert_called_with("Result:", result)