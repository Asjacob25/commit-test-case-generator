# tests/test_operations.py
import pytest
from utils.operations import add, subtract, multiply, divide, power

def test_add():
    """Test the add function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(-2, -3) == -5

def test_subtract():
    """Test the subtract function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    assert subtract(-3, -3) == 0
    assert subtract(-5, 5) == -10

def test_multiply():
    """Test the multiply function."""
    assert multiply(4, 3) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(-3, -3) == 9

def test_divide():
    """Test the divide function."""
    assert divide(10, 2) == 5
    assert divide(3, 2) == 1.5
    assert divide(-6, 2) == -3
    assert divide(0, 1) == 0

    # Test divide by zero case
    assert divide(5, 0) == "Cannot divide by zero"

def test_power():
    """Test the power function."""
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5
    assert power(0, 0) == 1  # Typically 0^0 is defined as 1 in most programming languages
    assert power(-2, 3) == -8
