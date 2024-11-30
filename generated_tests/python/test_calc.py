import pytest
from unittest.mock import patch
from operations import add, subtract, multiply, divide, power
from your_module import calculator  # Assuming the provided code is saved in your_module.py

# Test cases for operations.py

def test_add():
    assert add(1, 1) == 2
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(1, 1) == 0
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(-1, -1) == 1

def test_divide():
    assert divide(4, 2) == 2
    assert divide(5, 2) == 2.5
    assert divide(1, 0) == "Cannot divide by zero"

def test_power():
    assert power(2, 3) == 8
    assert power(-1, 2) == 1
    assert power(-2, -2) == 0.25

# Test cases for calculator function

@patch('builtins.input', side_effect=['1', '2', '3'])
@patch('builtins.print')
def test_calculator_add(mock_print, mock_inputs):
    calculator()
    mock_print.assert_called_with("Result:", 5)

@patch('builtins.input', side_effect=['2', '5', '3'])
@patch('builtins.print')
def test_calculator_subtract(mock_print, mock_inputs):
    calculator()
    mock_print.assert_called_with("Result:", 2)

@patch('builtins.input', side_effect=['3', '2', '3'])
@patch('builtins.print')
def test_calculator_multiply(mock_print, mock_inputs):
    calculator()
    mock_print.assert_called_with("Result:", 6)

@patch('builtins.input', side_effect=['4', '6', '3'])
@patch('builtins.print')
def test_calculator_divide_success(mock_print, mock_inputs):
    calculator()
    mock_print.assert_called_with("Result:", 2.0)

@patch('builtins.input', side_effect=['4', '6', '0'])
@patch('builtins.print')
def test_calculator_divide_by_zero(mock_print, mock_inputs):
    calculator()
    mock_print.assert_called_with("Result:", "Cannot divide by zero")

@patch('builtins.input', side_effect=['5', '2', '3'])
@patch('builtins.print')
def test_calculator_power(mock_print, mock_inputs):
    calculator()
    mock_print.assert_called_with("Result:", 8)

@patch('builtins.input', side_effect=['6'])
@patch('builtins.print')
def test_calculator_invalid_option(mock_print, mock_inputs):
    calculator()
    mock_print.assert_called_with("Invalid choice. Please select a valid option.")

@patch('builtins.input', side_effect=['1', 'a', 'b'])
@patch('builtins.print')
def test_calculator_invalid_number_input(mock_print, mock_inputs):
    calculator()
    mock_print.assert_called_with("Invalid input. Please enter numbers only.")