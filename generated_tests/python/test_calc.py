import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from unittest.mock import patch
from calc import calculator

# Note: Assuming operations are from a module utils.operations, based on provided context.
# Therefore, imports for operations (add, subtract, multiply, divide, power) are not directly used in test

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
def mock_input_divide_by_zero():
    with patch('builtins.input', side_effect=['4', '10', '0']):
        yield

@pytest.fixture
def mock_input_invalid_number():
    with patch('builtins.input', side_effect=['1', 'ten', 'five']):
        yield

@pytest.fixture
def mock_input_invalid_choice():
    with patch('builtins.input', side_effect=['6']):
        yield

def test_calculator_addition(mock_input_add, capsys):
    """Test calculator addition functionality with mock inputs"""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_subtraction(mock_input_subtract, capsys):
    """Test calculator subtraction functionality with mock inputs"""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_multiplication(mock_input_multiply, capsys):
    """Test calculator multiplication functionality with mock inputs"""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_division(mock_input_divide, capsys):
    """Test calculator division functionality with mock inputs"""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_power(mock_input_power, capsys):
    """Test calculator power functionality with mock inputs"""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_divide_by_zero(mock_input_divide_by_zero, capsys):
    """Test calculator division by zero functionality"""
    calculator()
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out

def test_calculator_invalid_number_input(mock_input_invalid_number, capsys):
    """Test calculator with invalid number inputs"""
    calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numbers only." in captured.out

def test_calculator_invalid_choice(mock_input_invalid_choice, capsys):
    """Test calculator with invalid operation choice"""
    calculator()
    captured = capsys.readouterr()
    assert "Invalid choice. Please select a valid option." in captured.out