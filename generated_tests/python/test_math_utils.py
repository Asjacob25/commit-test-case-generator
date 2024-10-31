import pytest
from unittest.mock import patch
from your_module import add, power, minusOne, subtract, multiply, divide, calculator

# Test for add function
def test_add_normal():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(0, 0) == 0

# Test for power function
def test_power_normal():
    assert power(2, 3) == 8

def test_power_zero_exponent():
    assert power(4, 0) == 1

def test_power_zero_base():
    assert power(0, 3) == 0

def test_power_negative_exponent():
    assert power(2, -2) == 0.25

# Test for minusOne function
def test_minusOne_normal():
    assert minusOne(5) == 4

def test_minusOne_zero():
    assert minusOne(0) == -1

def test_minusOne_negative():
    assert minusOne(-2) == -3

# Test for subtract function
def test_subtract_normal():
    assert subtract(5, 3) == 2

def test_subtract_negative_result():
    assert subtract(2, 5) == -3

def test_subtract_zero():
    assert subtract(0, 0) == 0

# Test for multiply function
def test_multiply_normal():
    assert multiply(3, 4) == 12

def test_multiply_by_zero():
    assert multiply(5, 0) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6

# Test for divide function
def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(5, 0) == "Error: Division by zero!"

def test_divide_zero_by_number():
    assert divide(0, 5) == 0

def test_divide_negative():
    assert divide(-10, 2) == -5

# Tests for calculator function using mocking for input and print
@patch('builtins.input', side_effect=['1', '10', '5', 'exit'])
@patch('builtins.print')
def test_calculator_addition(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("10.0 + 5.0 = 15.0")

@patch('builtins.input', side_effect=['2', '10', '5', 'exit'])
@patch('builtins.print')
def test_calculator_subtraction(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("10.0 - 5.0 = 5.0")

@patch('builtins.input', side_effect=['3', '10', '5', 'exit'])
@patch('builtins.print')
def test_calculator_multiplication(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("10.0 * 5.0 = 50.0")

@patch('builtins.input', side_effect=['4', '10', '5', 'exit'])
@patch('builtins.print')
def test_calculator_division(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("10.0 / 5.0 = 2.0")

@patch('builtins.input', side_effect=['4', '10', '0', 'exit'])
@patch('builtins.print')
def test_calculator_division_by_zero(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("10.0 / 0.0 = Error: Division by zero!")

@patch('builtins.input', side_effect=['5', 'exit'])  # Invalid choice
@patch('builtins.print')
def test_calculator_invalid_choice(mock_print, mock_input):
    calculator()
    mock_print.assert_any_call("Invalid input. Please enter a number from 1 to 4.")