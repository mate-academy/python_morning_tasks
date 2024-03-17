import subprocess

import length


VARIABLES = length
VAR_NAME = "goal_length"
EXPECTED_LEN = 60


def variables_are_defined():
    assert hasattr(VARIABLES, VAR_NAME), f"Failed. {VAR_NAME} should be defined"

    var_value = getattr(VARIABLES, VAR_NAME)
    assert isinstance(var_value, int), f"Failed. {VAR_NAME} should be <int> type"

    assert (
        var_value == EXPECTED_LEN
    ), f"Failed. {VAR_NAME} should be equal to {EXPECTED_LEN}. Output: {var_value}"


def variable_was_printed():
    process = subprocess.Popen(["python", "length.py"], stdout=subprocess.PIPE)

    captured_output = process.communicate()[0].decode()
    printed_output = captured_output.strip()

    assert printed_output == str(
        EXPECTED_LEN
    ), f"Failed. {VAR_NAME} should be printed. You printed: {printed_output} != {EXPECTED_LEN}"
