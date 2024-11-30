import pytest
from unittest.mock import patch
from your_module import add, subtract, multiply, divide, calculator, power

@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 15),
    (-1, 1, 0),
    (2.5, 2.5, 5.0),
])
def test_add(x, y, expected):
    """Test add function with normal and edge cases."""
    assert add(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 5),
    (-1, -1, 0),
    (2.5, 2.5, 0.0),
])
def test_subtract(x, y, expected):
    """Test subtract function with normal and edge cases."""
    assert subtract(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 50),
    (-1, 1, -1),
    (2.5, 2, 5.0),
])
def test_multiply(x, y, expected):
    """Test multiply function with normal and edge cases."""
    assert multiply(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 8),
    (-1, 0, 1),
    (10, -2, 0.01),
])
def test_power(x, y, expected):
    """Test power function with normal and edge cases."""
    assert power(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 2.0),
    (-1, 1, -1.0),
    (2.5, 0, "Cannot divide by zero"),
])
def test_divide(x, y, expected):
    """Test divide function with normal, edge, and error cases."""
    assert divide(x, y) == expected

@patch("builtins.input")
def test_calculator_add(mock_input):
    """Test calculator function for addition."""
    mock_input.side_effect = ["1", "10", "5"]
    with patch("builtins.print") as mock_print:
        calculator()
        mock_print.assert_called_with("Result:", 15)

@patch("builtins.input")
def test_calculator_subtract(mock_input):
    """Test calculator function for subtraction."""
    mock_input.side_effect = ["2", "10", "5"]
    with patch("builtins.print") as mock_print:
        calculator()
        mock_print.assert_called_with("Result:", 5)

@patch("builtins.input")
def test_calculator_multiply(mock_input):
    """Test calculator function for multiplication."""
    mock_input.side_effect = ["3", "10", "5"]
    with patch("builtins.print") as mock_print:
        calculator()
        mock_print.assert_called_with("Result:", 50)

@patch("builtins.input")
def test_calculator_divide(mock_input):
    """Test calculator function for division."""
    mock_input.side_effect = ["4", "10", "0"]
    with patch("builtins.print") as mock_print:
        calculator()
        mock_print.assert_called_with("Result:", "Cannot divide by zero")

@patch("builtins.input")
def test_calculator_invalid_choice(mock_input):
    """Test calculator function with an invalid choice."""
    mock_input.side_effect = ["5"]
    with patch("builtins.print") as mock_print:
        calculator()
        mock_print.assert_called_with("Invalid choice. Please select a valid option.")

@patch("builtins.input")
def test_calculator_invalid_number_input(mock_input):
    """Test calculator function with an invalid number input."""
    mock_input.side_effect = ["1", "ten", "5"]
    with patch("builtins.print") as mock_print:
        calculator()
        mock_print.assert_called_with("Invalid input. Please enter numbers only.")