import pytest
from unittest.mock import patch
from calculator_module import calculator  # Assuming the initial code is saved in calculator_module.py
from utils.operations import add, subtract, multiply, divide, power

@pytest.fixture
def mock_input(monkeypatch):
    def _mock_input(prompt, inputs):
        mock = iter(inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(mock))
    return _mock_input

@pytest.fixture
def mock_print(monkeypatch):
    prints = []
    monkeypatch.setattr('builtins.print', lambda *args: prints.append(args))
    return prints

# Test addition
@pytest.mark.parametrize("inputs,expected", [
    (('1', '2', '3'), "Result: 5.0"),
])
def test_addition(mock_input, mock_print, inputs, expected):
    """Test addition operation."""
    mock_input(inputs)
    calculator()
    assert mock_print[-1] == (expected,)

# Test subtraction
@pytest.mark.parametrize("inputs,expected", [
    (('2', '5', '2'), "Result: 3.0"),
])
def test_subtraction(mock_input, mock_print, inputs, expected):
    """Test subtraction operation."""
    mock_input(inputs)
    calculator()
    assert mock_print[-1] == (expected,)

# Test multiplication
@pytest.mark.parametrize("inputs,expected", [
    (('3', '3', '3'), "Result: 9.0"),
])
def test_multiplication(mock_input, mock_print, inputs, expected):
    """Test multiplication operation."""
    mock_input(inputs)
    calculator()
    assert mock_print[-1] == (expected,)

# Test division
@pytest.mark.parametrize("inputs,expected", [
    (('4', '10', '2'), "Result: 5.0"),
    (('4', '10', '0'), "Cannot divide by zero"),
])
def test_division(mock_input, mock_print, inputs, expected):
    """Test division operation."""
    mock_input(inputs)
    calculator()
    assert mock_print[-1] == (expected,)

# Test power
@pytest.mark.parametrize("inputs,expected", [
    (('5', '2', '3'), "Result: 8.0"),
])
def test_power(mock_input, mock_print, inputs, expected):
    """Test power operation."""
    mock_input(inputs)
    calculator()
    assert mock_print[-1] == (expected,)

# Test invalid choice
def test_invalid_choice(mock_input, mock_print):
    """Test with an invalid operation choice."""
    mock_input(('6',))
    calculator()
    assert mock_print[-1] == ("Invalid choice. Please select a valid option.",)

# Test invalid number input
@pytest.mark.parametrize("inputs", [
    ('1', 'a', '3'),
    ('1', '2', 'b'),
])
def test_invalid_number_input(mock_input, mock_print, inputs):
    """Test with invalid number inputs."""
    mock_input(inputs)
    calculator()
    assert mock_print[-1] == ("Invalid input. Please enter numbers only.",)

# Test division by zero handled in utils.operations (though already caught in test_division)
def test_division_by_zero_in_operations():
    """Check divide function directly for division by zero."""
    result = divide(10, 0)
    assert result == "Cannot divide by zero"