import subprocess

import upper


VARIABLES = upper
VAR_NAME = "last_name"


def test_variable_is_defined_as_uppercase_string():
    assert hasattr(
        VARIABLES, VAR_NAME
    ), f"Failed. Variable {VAR_NAME} should be defined."

    name_variable = getattr(VARIABLES, VAR_NAME)
    assert isinstance(
        name_variable, str
    ), f"Failed. Variable {VAR_NAME} should be an {str} data type"
    assert (
        name_variable == name_variable.upper()
    ), f"Failed. Variable {VAR_NAME} should contain your name in uppercase. {name_variable.upper()} != {name_variable}"


def test_variable_was_printed():
    process = subprocess.Popen(["python", "upper.py"], stdout=subprocess.PIPE)

    captured_output = process.communicate()[0].decode()
    printed_output = captured_output.strip()
    uppercase_name = getattr(VARIABLES, VAR_NAME).upper()

    assert (
        printed_output == uppercase_name
    ), f"Failed. Variable {VAR_NAME} should be printed out as uppercase string. You printed: {printed_output} != {uppercase_name}"
