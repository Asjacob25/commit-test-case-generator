# File: test_calc.py
import pytest
from unittest.mock import patch
from calc import calculator
from utils.operations import add, subtract, multiply, divide, power

@pytest.fixture
def mock_input():
    with patch('builtins.input', side_effect=['1', '3', '5']):
        yield

@pytest.fixture
def mock_add():
    with patch('utils.operations.add', return_value=8):
        yield

@pytest.fixture
def mock_subtract():
    with patch('utils.operations.subtract', return_value=-2):
        yield

@pytest.fixture
def mock_multiply():
    with patch('utils.operations.multiply', return_value=15):
        yield

@pytest.fixture
def mock_divide():
    with patch('utils.operations.divide', return_value=0.6):
        yield

@pytest.fixture
def mock_power():
    with patch('utils.operations.power', return_value=243):
        yield

def test_calculator_addition(mock_input, mock_add, capsys):
    """Test calculator addition functionality"""
    calculator()
    captured = capsys.readouterr()
    assert "Result: 8" in captured.out

def test_calculator_subtraction(mock_input, mock_subtract, capsys):
    """Test calculator subtraction functionality"""
    calculator()
    captured = capsys.readouterr()
    assert "Result: -2" in captured.out

def test_calculator_multiplication(mock_input, mock_multiply, capsys):
    """Test calculator multiplication functionality"""
    calculator()
    captured = capsys.readouterr()
    assert "Result: 15" in captured.out

def test_calculator_division(mock_input, mock_divide, capsys):
    """Test calculator division functionality"""
    calculator()
    captured = capsys.readouterr()
    assert "Result: 0.6" in captured.out

def test_calculator_power(mock_input, mock_power, capsys):
    """Test calculator power functionality"""
    calculator()
    captured = capsys.readouterr()
    assert "Result: 243" in captured.out

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

def test_calculator_divide_by_zero(capsys):
    """Test division by zero"""
    with patch('builtins.input', side_effect=['4', '5', '0']):
        calculator()
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out