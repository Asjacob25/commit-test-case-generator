import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from unittest.mock import patch
from calc import main

# Helper functions
def mock_inputs(inputs):
    """
    Mocks user input.
    """
    return patch('builtins.input', side_effect=inputs)

def mock_print():
    """
    Mocks the print function.
    """
    return patch('builtins.print')

# Test cases
@pytest.mark.parametrize("input_values, expected_output", [
    (("2", "3"), ["The sum is: 5.0", "The difference is: -1.0", "The product is: 6.0", "The quotient is: 0.6666666666666666"]),
    (("5", "0"), ["The sum is: 5.0", "The difference is: 5.0", "The product is: 0.0", "The quotient is: undefined (division by zero)"]),
    (("-1", "-2"), ["The sum is: -3.0", "The difference is: 1.0", "The product is: 2.0", "The quotient is: 0.5"]),
    (("1", "0"), ["The sum is: 1.0", "The difference is: 1.0", "The product is: 0.0", "The quotient is: undefined (division by zero)"]),
    (("0", "0"), ["The sum is: 0.0", "The difference is: 0.0", "The product is: 0.0", "The quotient is: undefined (division by zero)"]),
])
def test_main_normal_edge_and_special_cases(input_values, expected_output):
    """
    Tests normal, edge, and special cases for the main function.
    """
    with mock_inputs(input_values), mock_print() as mocked_print:
        main()
        mocked_print.assert_has_calls([patch.call(output) for output in expected_output], any_order=False)

@pytest.mark.parametrize("input_values, error_message", [
    (("a", "2"), ValueError),
    (("2", "b"), ValueError),
    (("a", "b"), ValueError),
])
def test_main_input_validation(input_values, error_message):
    """
    Tests input validation for the main function, expecting ValueError for non-numeric inputs.
    """
    with mock_inputs(input_values), pytest.raises(error_message):
        main()

@pytest.mark.parametrize("input_values", [
    ("2", "3"),
    ("5", "0"),
    ("-1", "-2"),
    ("1", "0"),
    ("0", "0"),
])
def test_main_no_exceptions(input_values):
    """
    Tests that no exceptions are raised for valid and special input cases.
    """
    with mock_inputs(input_values):
        try:
            main()
        except Exception as e:
            pytest.fail(f"Unexpected exception occurred: {e}")