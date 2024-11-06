import pytest
from unittest.mock import patch
from calc import calculator

@pytest.mark.parametrize("input_values, expected_output", [
    (['1', '3', '5'], "Result: 8\n"),
    (['2', '5', '3'], "Result: 2\n"),
    (['3', '2', '4'], "Result: 8\n"),
    (['4', '10', '2'], "Result: 5.0\n"),
    (['5', '2', '3'], "Result: 8\n"),
])
def test_calculator_operations(input_values, expected_output, capsys):
    """
    Test calculator with multiple operations
    """
    with patch('builtins.input', side_effect=input_values):
        calculator()
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test_calculator_invalid_choice(capsys):
    """
    Test calculator with invalid choice
    """
    with patch('builtins.input', side_effect=['6']):
        calculator()
    captured = capsys.readouterr()
    assert "Invalid choice. Please select a valid option.\n" == captured.out

def test_calculator_invalid_number_input(capsys):
    """
    Test calculator with invalid number input
    """
    with patch('builtins.input', side_effect=['1', 'a', 'b']):
        calculator()
    captured = capsys.readouterr()
    assert "Invalid input. Please enter numbers only.\n" == captured.out

def test_calculator_divide_by_zero(capsys):
    """
    Test division by zero
    """
    with patch('builtins.input', side_effect=['4', '5', '0']):
        calculator()
    captured = capsys.readouterr()
    assert "Cannot divide by zero\n" == captured.out

@pytest.mark.parametrize("operation, num1, num2, mock_return, expected", [
    ('1', '5', '3', 8, "Result: 8\n"),
    ('2', '5', '3', 2, "Result: 2\n"),
    ('3', '2', '4', 8, "Result: 8\n"),
    ('4', '10', '2', 5.0, "Result: 5.0\n"),
    ('5', '2', '3', 8, "Result: 8\n"),
])
def test_calculator_mock_operations(operation, num1, num2, mock_return, expected, capsys, mocker):
    """
    Test calculator operations with mocks
    """
    mocker.patch('builtins.input', side_effect=[operation, num1, num2])
    mocker.patch('utils.operations.add', return_value=mock_return)
    mocker.patch('utils.operations.subtract', return_value=mock_return)
    mocker.patch('utils.operations.multiply', return_value=mock_return)
    mocker.patch('utils.operations.divide', return_value=mock_return)
    mocker.patch('utils.operations.power', return_value=mock_return)
    
    calculator()
    captured = capsys.readouterr()
    assert captured.out == expected