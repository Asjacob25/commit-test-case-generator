import pytest
from unittest.mock import patch
from calc import calculator

# Adjusting the mock patch locations according to the provided code structure
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
def mock_input_divide_by_zero():
    with patch('builtins.input', side_effect=['4', '5', '0']):
        yield

@pytest.fixture
def mock_operations():
    with patch('operations.add', return_value=8), \
         patch('operations.subtract', return_value=5), \
         patch('operations.multiply', return_value=15), \
         patch('operations.divide', return_value=5), \
         patch('operations.power', return_value=8):
        yield

def test_calculator_addition(mock_input_add, mock_operations, capsys):
    """Test calculator addition functionality"""
    calculator()
    captured = capsys.readouterr()
    assert "Result: 8" in captured.out

def test_calculator_subtraction(mock_input_subtract, mock_operations, capsys):
    """Test calculator subtraction functionality"""
    calculator()
    captured = capsys.readouterr()
    assert "Result: 5" in captured.out

def test_calculator_multiplication(mock_input_multiply, mock_operations, capsys):
    """Test calculator multiplication functionality"""
    calculator()
    captured = capsys.readouterr()
    assert "Result: 15" in captured.out

def test_calculator_division(mock_input_divide, mock_operations, capsys):
    """Test calculator division functionality"""
    calculator()
    captured = capsys.readouterr()
    assert "Result: 5" in captured.out

def test_calculator_power(mock_input_power, mock_operations, capsys):
    """Test calculator power functionality"""
    calculator()
    captured = capsys.readouterr()
    assert "Result: 8" in captured.out

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

def test_calculator_divide_by_zero(mock_input_divide_by_zero, capsys):
    """Test division by zero scenario"""
    with patch('operations.divide', side_effect=ZeroDivisionError("Cannot divide by zero")):
        calculator()
    captured = capsys.readouterr()
    assert "Cannot divide by zero" in captured.out