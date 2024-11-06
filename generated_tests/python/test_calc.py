import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from unittest.mock import patch
from calc import calculator

@pytest.fixture
def mock_input_add():
    with patch('builtins.input', side_effect=['1', '3', '5']):
        yield

@pytest.fixture
def mock_input_subtract():
    with patch('builtins.input', side_effect=['2', '10', '5']):
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
    with patch('builtins.input', side_effect=['5', '2', '3']):
        yield

@pytest.fixture
def mock_input_invalid_choice():
    with patch('builtins.input', side_effect=['6']):
        yield

@pytest.fixture
def mock_input_invalid_number():
    with patch('builtins.input', side_effect=['1', 'a', '5']):
        yield

@pytest.fixture
def mock_input_divide_by_zero():
    with patch('builtins.input', side_effect=['4', '5', '0']):
        yield

@pytest.mark.usefixtures("mock_input_add")
def test_calculator_addition_success(capsys):
    """Test calculator handles addition correctly."""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

@pytest.mark.usefixtures("mock_input_subtract")
def test_calculator_subtraction_success(capsys):
    """Test calculator handles subtraction correctly."""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

@pytest.mark.usefixtures("mock_input_multiply")
def test_calculator_multiplication_success(capsys):
    """Test calculator handles multiplication correctly."""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

@pytest.mark.usefixtures("mock_input_divide")
def test_calculator_division_success(capsys):
    """Test calculator handles division correctly."""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

@pytest.mark.usefixtures("mock_input_power")
def test_calculator_power_success(capsys):
    """Test calculator handles power operation correctly."""
    calculator()
    captured = capsys.readouterr()
    assert "Result:" in captured.out

@pytest.mark.usefixtures("mock_input_invalid_choice")
def test_calculator_invalid_choice(capsys):
    """Test calculator with invalid operation choice."""
    calculator()
    captured = capsys.readouterr()
    assert "Invalid choice. Please select a valid option." in captured.out

@pytest.mark.usefixtures("mock_input_invalid_number")
def test_calculator_invalid_number_input(capsys):
    """Test calculator with non-numeric inputs."""
    calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numbers only." in captured.out

@pytest.mark.usefixtures("mock_input_divide_by_zero")
def test_calculator_divide_by_zero(capsys):
    """Test calculator handles division by zero appropriately."""
    calculator()
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out