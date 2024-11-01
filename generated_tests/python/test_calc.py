# Import pytest and the mock patch method
import pytest
from unittest.mock import patch
from operations import add, subtract, multiply, divide, power

# Test suite for the calculator function
@pytest.mark.parametrize("input,expected_output", [
    (("1\n2\n3",), "Result: 5.0\n"),
    (("2\n5\n3",), "Result: 2.0\n"),
    (("3\n6\n2",), "Result: 12.0\n"),
    (("4\n8\n2",), "Result: 4.0\n"),
    (("5\n2\n3",), "Result: 8.0\n"),
    (("6",), "Invalid choice. Please select a valid option.\n"),
    (("1\na\n3",), "Invalid input. Please enter numbers only.\n"),
    (("4\n10\n0",), "Result: Cannot divide by zero\n"),
])
def test_calculator_operations(input, expected_output, capsys):
    """
    Test normal and edge cases for calculator operations including invalid choices and inputs.
    """
    with patch('builtins.input', side_effect=input.split("\n")):
        from calculator import calculator
        calculator()
        captured = capsys.readouterr()
        assert captured.out == expected_output

@pytest.mark.parametrize("operation, num1, num2, expected", [
    (add, 1, 2, 3),
    (subtract, 5, 3, 2),
    (multiply, 4, 5, 20),
    (divide, 8, 2, 4),
    (divide, 8, 0, "Cannot divide by zero"),
    (power, 2, 3, 8),
])
def test_operations_success(operation, num1, num2, expected):
    """
    Test success scenarios for all operations.
    """
    assert operation(num1, num2) == expected

@pytest.mark.parametrize("operation, num1, num2", [
    (divide, 10, 0),
    (add, 'a', 2),
    (subtract, 5, 'b'),
    (multiply, 'x', 'y'),
    (power, 'base', 'exp')
])
def test_operations_failure(operation, num1, num2):
    """
    Test failure scenarios for operations with invalid inputs.
    This test assumes that operations will raise a TypeError for invalid inputs,
    which is not currently handled in the code. This is to demonstrate how to write
    failure scenario tests assuming the code is supposed to handle such cases.
    """
    with pytest.raises(TypeError):
        operation(num1, num2)