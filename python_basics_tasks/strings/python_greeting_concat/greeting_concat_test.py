import subprocess

import greeting_concat


VARIABLES = greeting_concat
FIRST_NAME_VAR = "first_name"
RESULT_VAR = "greeting"


def test_all_variables_defined():
    assert hasattr(
        VARIABLES, FIRST_NAME_VAR
    ), f"Failed. Variable {FIRST_NAME_VAR} should be defined"
    assert hasattr(
        VARIABLES, RESULT_VAR
    ), f"Failed. Variable {RESULT_VAR} should be defined"

    first_name = getattr(VARIABLES, FIRST_NAME_VAR)
    greeting = getattr(VARIABLES, RESULT_VAR)

    assert isinstance(
        first_name, str
    ), f"Failed. Variable {FIRST_NAME_VAR} should be <str> type"
    assert isinstance(
        greeting, str
    ), f"Failed. Variable {RESULT_VAR} should be <str> type"

    expected = f"Hello, {first_name}!"
    assert (
        greeting == expected
    ), f"Failed. Variable {RESULT_VAR} should contain {expected} string. {greeting} != {expected}"


def test_greeting_was_printed():
    process = subprocess.Popen(["python", "greeting_concat.py"], stdout=subprocess.PIPE)

    captured_output = process.communicate()[0].decode()
    printed_output = captured_output.strip()

    first_name = getattr(VARIABLES, FIRST_NAME_VAR)
    expected = f"Hello, {first_name}!"

    assert printed_output == expected, f"Failed. {RESULT_VAR} should be printed out."
