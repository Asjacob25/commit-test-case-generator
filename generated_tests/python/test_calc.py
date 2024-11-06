import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from unittest.mock import patch
from calc import calculator
from utils.operations import add, subtract, multiply, divide, power

@pytest.fixture
def mock_input_add():
    with patch('builtins.input', side_effect=['1', '3', '5']):
        yield

@pytest.fixture
def mock_input_subtract():
    with patch('builtins.input', side_effect=['2', '10', '2']):
        yield

@pytest.fixture
def mock_input_multiply():
    with patch('builtins.input', side_effect=['3', '3', '5']):
        yield

@pytest.fixture
def mock_input_divide():
    with patch('builtins.input', side_effect=['4', '10', '2']):
        yield

@pytest.fixture
def mock_input_power():
    with patch('builtins.input', side_effect=['5', '3', '3']):
        yield

@pytest.fixture
def mock_input_divide_by_zero():
    with patch('builtins.input', side_effect=['4', '5', '0']):
        yield

@pytest.fixture
def mock_invalid_choice():
    with patch('builtins.input', side_effect=['6']):
        yield

@pytest.fixture
def mock_invalid_number():
    with patch('builtins.input', side_effect=['1', 'a', '5']):
        yield

def test_calculator_addition(mock_input_add, capsys):
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_subtraction(mock_input_subtract, capsys):
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_multiplication(mock_input_multiply, capsys):
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_division(mock_input_divide, capsys):
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_power(mock_input_power, capsys):
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

def test_calculator_divide_by_zero(mock_input_divide_by_zero, capsys):
    calculator()
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out

def test_calculator_invalid_choice(mock_invalid_choice, capsys):
    calculator()
    captured = capsys.readouterr()
    assert "Invalid choice. Please select a valid option." in captured.out

def test_calculator_invalid_number_input(mock_invalid_number, capsys):
    calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numbers only." in captured.out