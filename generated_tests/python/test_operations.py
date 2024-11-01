import pytest
from operations import add, subtract, multiply, power, divide

# Test suite for operations.py

@pytest.fixture(scope="module")
def setup_teardown():
    # Setup before any tests run
    print("\nSetup before tests")
    yield
    # Teardown after all tests are done
    print("\nTeardown after tests")

class TestAdd:
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        assert add(-2, -3) == -5

    def test_add_positive_and_negative(self):
        """Test adding a positive and a negative number."""
        assert add(-2, 3) == 1

    def test_add_zero(self):
        """Test adding zero."""
        assert add(0, 0) == 0

class TestSubtract:
    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2

    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        assert subtract(-5, -3) == -2

    def test_subtract_positive_and_negative(self):
        """Test subtracting a positive and a negative number."""
        assert subtract(5, -3) == 8

    def test_subtract_with_zero(self):
        """Test subtracting zero."""
        assert subtract(0, 0) == 0

class TestMultiply:
    def test_multiply_two_positive_numbers(self):
        """Test multiplying two positive numbers."""
        assert multiply(2, 3) == 6

    def test_multiply_two_negative_numbers(self):
        """Test multiplying two negative numbers."""
        assert multiply(-2, -3) == 6

    def test_multiply_positive_and_negative(self):
        """Test multiplying a positive and a negative number."""
        assert multiply(-2, 3) == -6

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(0, 3) == 0
        assert multiply(3, 0) == 0

class TestPower:
    def test_power_positive(self):
        """Test raising a positive number to a power."""
        assert power(2, 3) == 8

    def test_power_zero(self):
        """Test raising zero to a power."""
        assert power(0, 3) == 0

    def test_power_negative_exponent(self):
        """Test raising a number to a negative power."""
        assert power(2, -3) == pytest.approx(0.125)

    def test_power_zero_exponent(self):
        """Test raising a number to the power of zero."""
        assert power(2, 0) == 1

class TestDivide:
    def test_divide_two_positive_numbers(self):
        """Test dividing two positive numbers."""
        assert divide(4, 2) == 2

    def test_divide_by_zero(self):
        """Test dividing by zero returns an error message."""
        assert divide(4, 0) == "Cannot divide by zero"

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 3) == 0

    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        assert divide(-4, -2) == 2

    def test_divide_positive_and_negative(self):
        """Test dividing a positive by a negative number (and vice versa)."""
        assert divide(-4, 2) == -2
        assert divide(4, -2) == -2

# This can be expanded to include more edge cases or test for exceptions
# in case the code changes to raise exceptions instead of returning strings.