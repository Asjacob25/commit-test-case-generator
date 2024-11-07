import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pytest
from unittest.mock import patch
from click.formatting import measure_table, iter_rows, wrap_text, HelpFormatter, join_options


@pytest.fixture
def setup_forced_width():
    from click.formatting import FORCED_WIDTH
    original_width = FORCED_WIDTH
    FORCED_WIDTH = 80
    yield
    FORCED_WIDTH = original_width


def test_measure_table_with_uniform_rows():
    rows = [("command", "description"), ("test", "test description")]
    assert measure_table(rows) == (7, 17)


def test_measure_table_with_varying_lengths():
    rows = [("short", "description"), ("longerCommandName", "description")]
    assert measure_table(rows) == (16, 11)


def test_measure_table_empty():
    rows = []
    assert measure_table(rows) == ()


def test_iter_rows_uniform_length():
    rows = [("command", "description"), ("test", "test description")]
    assert list(iter_rows(rows, 2)) == rows


def test_iter_rows_missing_columns():
    rows = [("command",), ("test", "test description")]
    assert list(iter_rows(rows, 2)) == [("command", ""), ("test", "test description")]


def test_wrap_text_normal():
    text = "This is a test."
    expected = "This is a test."
    assert wrap_text(text, 20) == expected


def test_wrap_text_preserve_paragraphs():
    text = "This is a paragraph.\n\nThis is another."
    expected = "This is a paragraph.\n\nThis is another."
    assert wrap_text(text, 20, preserve_paragraphs=True) == expected


def test_wrap_text_no_preserve_paragraphs():
    text = "This is a paragraph.\n\nThis is another."
    expected = "This is a paragraph. This is another."
    assert wrap_text(text, 50) == expected


@pytest.mark.parametrize("input_text,expected", [
    ("This\tis indented.", "This    is indented."),
    ("This is a long text that will be wrapped accordingly to the width provided.", "This is a long text that\nwill be wrapped accordingly\nto the width provided.")
])
def test_wrap_text_with_tabs_and_wrapping(input_text, expected):
    assert wrap_text(input_text, width=30) == expected


@pytest.fixture
def help_formatter():
    return HelpFormatter()


def test_help_formatter_initialization():
    formatter = HelpFormatter()
    assert formatter.indent_increment == 2
    assert formatter.width is not None


def test_help_formatter_write_usage(help_formatter):
    help_formatter.write_usage(prog="test", args="<command>")
    assert "Usage: test <command>" in help_formatter.getvalue()


def test_help_formatter_write_heading(help_formatter):
    help_formatter.write_heading("Heading")
    assert "Heading:\n" in help_formatter.getvalue()


def test_help_formatter_write_text(help_formatter):
    help_formatter.write_text("This is a test.")
    assert "This is a test.\n" in help_formatter.getvalue()


@pytest.mark.usefixtures("setup_forced_width")
def test_help_formatter_with_forced_width():
    formatter = HelpFormatter()
    assert formatter.width == 80


def test_help_formatter_write_dl(help_formatter):
    rows = [("command", "description"), ("test", "test description")]
    help_formatter.write_dl(rows)
    value = help_formatter.getvalue()
    assert "command" in value and "description" in value and "test description" in value


def test_join_options_simple():
    options = ["--help", "-h"]
    formatted, any_slash = join_options(options)
    assert formatted == "-h, --help"
    assert not any_slash


def test_join_options_with_slash_prefix():
    options = ["/help", "--help"]
    formatted, any_slash = join_options(options)
    assert formatted == "/help, --help"
    assert any_slash