import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# test_calc_2.py

import pytest
from unittest.mock import patch
from calc_2 import calculator
from utils.operations import add, subtract, multiply, divide, power

@pytest.fixture
def mock_input():
    with patch("builtins.input") as mocked_input:
        yield mocked_input

@pytest.fixture
def mock_print(mocker):
    return mocker.patch("builtins.print")

def test_calculator_addition(mock_input, mock_print):
    """
    Test calculator function for addition
    """
    mock_input.side_effect = ["1", "5", "3"]
    calculator()
    mock_print.assert_called_with("Result:", add(5, 3))

def test_calculator_subtraction(mock_input, mock_print):
    """
    Test calculator function for subtraction
    """
    mock_input.side_effect = ["2", "10", "3"]
    calculator()
    mock_print.assert_called_with("Result:", subtract(10, 3))

def test_calculator_multiplication(mock_input, mock_print):
    """
    Test calculator function for multiplication
    """
    mock_input.side_effect = ["3", "6", "2"]
    calculator()
    mock_print.assert_called_with("Result:", multiply(6, 2))

def test_calculator_division_success(mock_input, mock_print):
    """
    Test calculator function for successful division
    """
    mock_input.side_effect = ["4", "8", "2"]
    calculator()
    mock_print.assert_called_with("Result:", divide(8, 2))

def test_calculator_division_by_zero(mock_input, mock_print):
    """
    Test calculator function for division by zero
    """
    mock_input.side_effect = ["4", "5", "0"]
    calculator()
    mock_print.assert_called_with("Result:", "Cannot divide by zero")

def test_calculator_power_function(mock_input, mock_print):
    """
    Test calculator function for power operation
    """
    mock_input.side_effect = ["5", "2", "3"]
    calculator()
    mock_print.assert_called_with("Result:", power(2, 3))

def test_calculator_invalid_option(mock_input, mock_print):
    """
    Test calculator with an invalid option
    """
    mock_input.side_effect = ["6"]
    calculator()
    mock_print.assert_called_with("Invalid choice. Please select a valid option.")

def test_calculator_invalid_numeric_input(mock_input, mock_print):
    """
    Test calculator with invalid numeric input
    """
    mock_input.side_effect = ["1", "a", "b"]
    calculator()
    mock_print.assert_called_with("Invalid input. Please enter numbers only.")