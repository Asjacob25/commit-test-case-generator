import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import pytest
from unittest.mock import patch
#from calculator import main  # Assuming the given code is saved in calculator
from calc import main


# Helper function to simulate input for main()
def mock_inputs(inputs):
    return patch('builtins.input', side_effect=inputs)

# Helper function to simulate print
def mock_print():
    return patch('builtins.print')

@pytest.mark.parametrize("input_values, expected_output", [
    (("2", "3"), ["The sum is: 5.0", "The difference is: -1.0", "The product is: 6.0", "The quotient is: 0.6666666666666666"]),
    (("5", "0"), ["The sum is: 5.0", "The difference is: 5.0", "The product is: 0.0", "The quotient is: undefined (division by zero)"]),
    (("-1", "-2"), ["The sum is: -3.0", "The difference is: 1.0", "The product is: 2.0", "The quotient is: 0.5"]),
])

def test_main_normal_and_edge_cases(input_values, expected_output):
    """
    Test normal and edge cases for main function. It checks if the sum, difference, product,
    and quotient are correctly calculated and printed.
    """
    with mock_inputs(input_values), mock_print() as mocked_print:
        main()
        mocked_print.assert_has_calls([patch.call(output) for output in expected_output])

@pytest.mark.parametrize("input_values, error_message", [
    (("a", "2"), ValueError),
    (("2", "b"), ValueError),
])
def test_main_error_cases(input_values, error_message):
    """
    Test error cases for main function. It should raise a ValueError if the inputs
    are not convertible to float.
    """
    with mock_inputs(input_values), pytest.raises(error_message):
        main()

@pytest.mark.parametrize("input_values", [
    ("2", "3"),
    ("5", "0"),
    ("-1", "-2"),
])
def test_main_success(input_values):
    """
    Test success scenarios for main function to ensure no exceptions are raised
    for valid inputs.
    """
    with mock_inputs(input_values):
        try:
            main()
        except Exception as e:
            pytest.fail(f"Unexpected exception occurred: {e}")

@pytest.mark.parametrize("input_values", [
    ("1", "0"),
    ("0", "0"),
])
def test_division_by_zero(input_values):
    """
    Specifically testing division by zero scenarios to ensure the output
    is "undefined (division by zero)".
    """
    expected_output = "The quotient is: undefined (division by zero)"
    with mock_inputs(input_values), mock_print() as mocked_print:
        main()
        mocked_print.assert_any_call(expected_output)

#This test suite covers normal, edge, and error cases for the simple calculator script, including mocking user inputs and print statements to validate output without needing user interaction. It also handles division by zero and input type errors effectively.
