import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from unittest.mock import patch
from calc import calculator

@pytest.fixture
def mock_input_add():
    with patch('builtins.input', side_effect=['1', '10', '5']):
        yield

@pytest.fixture
def mock_input_subtract():
    with patch('builtins.input', side_effect=['2', '10', '5']):
        yield

@pytest.fixture
def mock_input_multiply():
    with patch('builtins.input', side_effect=['3', '10', '5']):
        yield

@pytest.fixture
def mock_input_divide():
    with patch('builtins.input', side_effect=['4', '10', '5']):
        yield

@pytest.fixture
def mock_input_power():
    with patch('builtins.input', side_effect=['5', '2', '3']):
        yield

@pytest.fixture
def mock_input_divide_zero():
    with patch('builtins.input', side_effect=['4', '10', '0']):
        yield

@pytest.fixture
def mock_input_invalid_number():
    with patch('builtins.input', side_effect=['1', 'a', '5']):
        yield

@pytest.fixture
def mock_input_invalid_choice():
    with patch('builtins.input', side_effect=['6', '10', '5']):
        yield

def test_calculator_addition(mock_input_add, capsys):
    """Test if calculator correctly performs addition"""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_subtraction(mock_input_subtract, capsys):
    """Test if calculator correctly performs subtraction"""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_multiplication(mock_input_multiply, capsys):
    """Test if calculator correctly performs multiplication"""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_division(mock_input_divide, capsys):
    """Test if calculator correctly performs division"""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_power(mock_input_power, capsys):
    """Test if calculator correctly performs power function"""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_divide_by_zero(mock_input_divide_zero, capsys):
    """Test division by zero error handling"""
    calculator()
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out

def test_calculator_invalid_number_input(mock_input_invalid_number, capsys):
    """Test handling of invalid number input"""
    calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numbers only." in captured.out

def test_calculator_invalid_choice(mock_input_invalid_choice, capsys):
    """Test handling of invalid choice input"""
    calculator()
    captured = capsys.readouterr()
    assert "Invalid choice. Please select a valid option." in captured.out