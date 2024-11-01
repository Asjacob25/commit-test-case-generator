# test_calculator.py
import pytest
from unittest.mock import patch
from calculator import calculator
from operations import add, subtract, multiply, divide, power

@pytest.fixture
def mock_input(monkeypatch):
    def _mock_input(mock_prompts):
        inputs = mock_prompts.copy()  # Copy the list to avoid modifying the original data

        def mock_input(_):
            return inputs.pop(0)
        monkeypatch.setattr("builtins.input", mock_input)
    return _mock_input

@pytest.fixture
def mock_print(monkeypatch):
    prints = []
    monkeypatch.setattr("builtins.print", prints.append)
    return prints

# Test add operation
@pytest.mark.parametrize("num1, num2, expected", [(1, 2, 3), (1.5, 2.5, 4)])
def test_add_success(mock_input, mock_print, num1, num2, expected):
    mock_input(['1', str(num1), str(num2)])
    calculator()
    assert mock_print[-1] == f"Result: {expected}"

# Test subtract operation
@pytest.mark.parametrize("num1, num2, expected", [(5, 3, 2), (2.5, 1.5, 1)])
def test_subtract_success(mock_input, mock_print, num1, num2, expected):
    mock_input(['2', str(num1), str(num2)])
    calculator()
    assert mock_print[-1] == f"Result: {expected}"

# Test multiply operation
@pytest.mark.parametrize("num1, num2, expected", [(2, 3, 6), (1.5, 2, 3)])
def test_multiply_success(mock_input, mock_print, num1, num2, expected):
    mock_input(['3', str(num1), str(num2)])
    calculator()
    assert mock_print[-1] == f"Result: {expected}"

# Test divide operation
@pytest.mark.parametrize("num1, num2, expected", [(6, 3, 2), (3, 2, 1.5)])
def test_divide_success(mock_input, mock_print, num1, num2, expected):
    mock_input(['4', str(num1), str(num2)])
    calculator()
    assert mock_print[-1] == f"Result: {expected}"

# Test divide by zero
def test_divide_by_zero(mock_input, mock_print):
    mock_input(['4', '1', '0'])
    calculator()
    assert mock_print[-1] == "Result: Cannot divide by zero"

# Test power operation
@pytest.mark.parametrize("num1, num2, expected", [(2, 3, 8), (3, 2, 9)])
def test_power_success(mock_input, mock_print, num1, num2, expected):
    mock_input(['5', str(num1), str(num2)])
    calculator()
    assert mock_print[-1] == f"Result: {expected}"

# Test invalid operation choice
def test_invalid_choice(mock_input, mock_print):
    mock_input(['6'])
    calculator()
    assert mock_print[-1] == "Invalid choice. Please select a valid option."

# Test invalid number input
@pytest.mark.parametrize("num1, num2", [('a', '2'), ('1', 'b')])
def test_invalid_number_input(mock_input, mock_print, num1, num2):
    mock_input(['1', num1, num2])
    calculator()
    assert mock_print[-1] == "Invalid input. Please enter numbers only."