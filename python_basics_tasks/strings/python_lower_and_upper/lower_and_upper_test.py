import subprocess

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
    process = subprocess.Popen(["python", "lower_and_upper.py"], stdout=subprocess.PIPE)

    captured_output = process.communicate()[0].decode()
    printed_output = captured_output.strip()
    lowered_name = getattr(VARIABLES, VAR_NAME).lower()

    assert (
        printed_output == lowered_name
    ), f"Failed. Variable {VAR_NAME} should be printed out as lowercase string. You printed: {printed_output} != {lowered_name}"
