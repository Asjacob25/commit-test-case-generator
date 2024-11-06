import pytest

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from utils.operations import add, subtract, multiply, power, divide

# Test cases for add function
@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 15),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_normal_cases(x, y, expected):
    """Test normal cases for the add function."""
    assert add(x, y) == expected

# Test cases for subtract function
@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 5),
    (-1, -1, 0),
    (0, 0, 0),
])
def test_subtract_normal_cases(x, y, expected):
    """Test normal cases for the subtract function."""
    assert subtract(x, y) == expected

# Test cases for multiply function
@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 50),
    (-1, 2, -2),
    (0, 10, 0),
])
def test_multiply_normal_cases(x, y, expected):
    """Test normal cases for the multiply function."""
    assert multiply(x, y) == expected

# Test cases for power function
@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 8),
    (-1, 2, 1),
    (10, 0, 1),
])
def test_power_normal_cases(x, y, expected):
    """Test normal cases for the power function."""
    assert power(x, y) == expected

# Test cases for divide function
@pytest.mark.parametrize("x, y, expected", [
    (10, 5, 2),
    (-1, 1, -1),
    (0, 10, 0),
])
def test_divide_normal_cases(x, y, expected):
    """Test normal cases for the divide function."""
    assert divide(x, y) == expected

def test_divide_by_zero():
    """Test divide function when dividing by zero."""
    assert divide(10, 0) == "Cannot divide by zero"

# Test cases for error scenarios
@pytest.mark.parametrize("x, y", [
    ("a", 5),
    (10, "b"),
])
def test_add_with_non_numeric_types(x, y):
    """Test add function with non-numeric types to ensure it raises TypeError."""
    with pytest.raises(TypeError):
        add(x, y)

@pytest.mark.parametrize("x, y", [
    ("a", 5),
    (10, "b"),
])
def test_subtract_with_non_numeric_types(x, y):
    """Test subtract function with non-numeric types to ensure it raises TypeError."""
    with pytest.raises(TypeError):
        subtract(x, y)

@pytest.mark.parametrize("x, y", [
    ("a", 5),
    (10, "b"),
])
def test_multiply_with_non_numeric_types(x, y):
    """Test multiply function with non-numeric types to ensure it raises TypeError."""
    with pytest.raises(TypeError):
        multiply(x, y)

@pytest.mark.parametrize("x, y", [
    ("a", 2),
    (2, "b"),
])
def test_power_with_non_numeric_types(x, y):
    """Test power function with non-numeric types to ensure it raises TypeError."""
    with pytest.raises(TypeError):
        power(x, y)

@pytest.mark.parametrize("x, y", [
    ("a", 5),
    (10, "b"),
])
def test_divide_with_non_numeric_types(x, y):
    """Test divide function with non-numeric types to ensure it raises TypeError."""
    with pytest.raises(TypeError):
        divide(x, y)
