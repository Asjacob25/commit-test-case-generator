import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from utils.operations import add, subtract, multiply, divide, power

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (1000000000000, 1000000000000, 2000000000000),
    (0, 0, 0)
])
def test_add(a, b, expected):
    """Test addition with normal, edge and large values."""
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (3, 2, 1),
    (-1, -2, 1),
    (-2, 1, -3),
    (0, 0, 0)
])
def test_subtract(a, b, expected):
    """Test subtraction with normal, edge and negative values."""
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (-1, -2, 2),
    (-2, 3, -6),
    (0, 10, 0),
    (10, 0, 0)
])
def test_multiply(a, b, expected):
    """Test multiplication with normal, edge and zero values."""
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 8),
    (-1, 3, -1),
    (2, -1, 0.5),
    (2, 0, 1)  # As per math, any number to the power of 0 is 1
])
def test_power(a, b, expected):
    """Test power function with normal, negative and zero exponent."""
    assert power(a, b) == expected

@pytest.mark.parametrize("a,b,expected", [
    (6, 3, 2),
    (-6, -3, 2),
    (-6, 3, -2),
    (0, 1, 0),
    (5, 2, 2.5)
])
def test_divide(a, b, expected):
    """Test division with normal, negative, and zero numerator."""
    assert divide(a, b) == expected

def test_divide_by_zero():
    """Test division by zero returns specific error message."""
    assert divide(5, 0) == "Cannot divide by zero"