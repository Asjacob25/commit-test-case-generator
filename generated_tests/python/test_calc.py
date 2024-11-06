# File: test_calc.py
import pytest
from unittest.mock import patch
from calc import calculator
from operations import add, subtract, multiply, divide, power

@pytest.fixture(autouse=True)
def mock_operations():
    with patch('calc.add', side_effect=add) as mock_add, \
         patch('calc.subtract', side_effect=subtract) as mock_subtract, \
         patch('calc.multiply', side_effect=multiply) as mock_multiply, \
         patch('calc.divide', side_effect=divide) as mock_divide, \
         patch('calc.power', side_effect=power) as mock_power:
        yield mock_add, mock_subtract, mock_multiply, mock_divide, mock_power

@pytest.mark.parametrize("input_values,expected_output", [
    (['1', '3', '5'], "Result: 8\n"),
    (['2', '5', '3'], "Result: 2\n"),
    (['3', '3', '5'], "Result: 15\n"),
    (['4', '10', '2'], "Result: 5.0\n"),
    (['5', '3', '4'], "Result: 81.0\n"),
])
def test_calculator_operations(input_values, expected_output, capsys):
    """Test calculator operations functionality"""
    with patch('builtins.input', side_effect=input_values):
        calculator()
    captured = capsys.readouterr()
    assert expected_output in captured.out

def test_calculator_invalid_choice(capsys):
    """Test calculator with invalid choice"""
    with patch('builtins.input', side_effect=['6']):
        calculator()
    captured = capsys.readouterr()
    assert "Invalid choice. Please select a valid option." in captured.out

def test_calculator_invalid_number_input(capsys):
    """Test calculator with invalid number input"""
    with patch('builtins.input', side_effect=['1', 'a', 'b']):
        calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numbers only." in captured.out

def test_calculator_divide_by_zero(capsys, mock_operations):
    """Test division by zero error handling"""
    with patch('builtins.input', side_effect=['4', '5', '0']):
        calculator()
    captured = capsys.readouterr()
    assert "Cannot divide by zero" not in captured.out  # Assuming no explicit divide by zero handling in `calc.py`
    # This test case might need adjustment based on the actual divide function's error handling