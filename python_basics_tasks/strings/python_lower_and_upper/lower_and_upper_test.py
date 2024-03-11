import sys

from io import StringIO

import lower_and_upper


VARIABLES = lower_and_upper
VAR_NAME = "first_name"


def test_variable_is_defined_as_lowercase_string():
    assert hasattr(
        VARIABLES, VAR_NAME
    ), f"Failed. Variable {VAR_NAME} should be defined."

    name_variable = getattr(VARIABLES, "first_name")
    assert isinstance(
        name_variable, str
    ), f"Failed. Variable {VAR_NAME} should be an {str} data type"
    assert (
        name_variable == name_variable.lower()
    ), f"Failed. Variable {VAR_NAME} should contain your name in lowercase. {name_variable.lower()} != {name_variable}"


def test_variable_was_printed():
    captured_output = StringIO()
    sys.stdout = captured_output

    exec(open("lower_and_upper.py").read())
    printed_output = captured_output.getvalue().strip()
    sys.stdout = sys.__stdout__

    lowered_name = getattr(VARIABLES, VAR_NAME).lower()
    assert (
        printed_output == lowered_name
    ), f"Failed. Variable {VAR_NAME} should be printed out as lowercase string. You printed: {printed_output} != {lowered_name}"
