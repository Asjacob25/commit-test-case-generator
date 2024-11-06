# File: test_operations.py

import pytest
from utils.operations import add, subtract, multiply, power, divide

# Test cases for add function
@pytest.mark.parametrize("x, y, expected", [
    (1, 2, 3),  # normal case
    (-1, -2, -3),  # negative numbers
    (0, 0, 0),  # edge case with zeros
    (1.5, 2.5, 4)  # floating point numbers
])
def test_add(x, y, expected):
    """Test addition with both normal and edge cases."""
    assert add(x, y) == expected

# Test cases for subtract function
@pytest.mark.parametrize("x, y, expected", [
    (5, 3, 2),  # normal case
    (-1, -2, 1),  # negative numbers
    (0, 0, 0),  # edge case with zeros
    (5.5, 2.2, 3.3)  # floating point numbers
])
def test_subtract(x, y, expected):
    """Test subtraction with both normal and edge cases."""
    assert subtract(x, y) == expected

# Test cases for multiply function
@pytest.mark.parametrize("x, y, expected", [
    (3, 4, 12),  # normal case
    (-1, 2, -2),  # negative numbers
    (0, 5, 0),  # edge case with zero
    (1.5, 4, 6)  # floating point numbers
])
def test_multiply(x, y, expected):
    """Test multiplication with both normal and edge cases."""
    assert multiply(x, y) == expected

# Test cases for power function
@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 8),  # normal case
    (2, -1, 0.5),  # negative exponent
    (1, 0, 1),  # edge case with zero exponent
    (2, 0.5, 1.4142135623730951)  # fractional exponent
])
def test_power(x, y, expected):
    """Test power function with both normal and edge cases."""
    assert power(x, y) == expected

# Test cases for divide function
@pytest.mark.parametrize("x, y, expected", [
    (4, 2, 2),  # normal case
    (-1, -1, 1),  # negative numbers
    (5.5, 2.2, 2.5),  # floating point numbers
])
def test_divide_success(x, y, expected):
    """Test division with normal cases."""
    assert divide(x, y) == expected

def test_divide_by_zero():
    """Test division by zero."""
    assert divide(5, 0) == "Cannot divide by zero"

# Example of using mocking (though not required for these specific tests)
def test_divide_mocking(mocker):
    """Mocking example, not directly applicable here as there's no external dependency to mock."""
    mocker.patch('utils.operations.divide', return_value=5)
    assert divide(10, 2) == 5