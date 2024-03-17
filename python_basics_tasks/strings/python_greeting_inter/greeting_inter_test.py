import re
import subprocess

import greeting_inter


TESTED_FILE = greeting_inter
FIRST_NAME_VAR = "first_name"
RESULT_VAR = "greeting"


def test_all_variables_defined():
    assert hasattr(
        TESTED_FILE, FIRST_NAME_VAR
    ), f"Failed. Variable '{FIRST_NAME_VAR}' should be defined"
    assert hasattr(
        TESTED_FILE, RESULT_VAR
    ), f"Failed. Variable '{RESULT_VAR}' should be defined"

    first_name = getattr(TESTED_FILE, FIRST_NAME_VAR)
    greeting = getattr(TESTED_FILE, RESULT_VAR)

    assert isinstance(
        first_name, str
    ), f"Failed. Variable '{FIRST_NAME_VAR}' should be <str> type"
    assert isinstance(
        greeting, str
    ), f"Failed. Variable '{RESULT_VAR}' should be <str> type"

    expected = f"Hello, {first_name}!"
    assert (
        greeting == expected
    ), f"Failed. Variable '{RESULT_VAR}' should contain {expected} string. {greeting} != {expected}"


def test_greeting_was_printed():
    process = subprocess.Popen(["python", "greeting_inter.py"], stdout=subprocess.PIPE)

    captured_output = process.communicate()[0].decode()
    printed_output = captured_output.strip()

    first_name = getattr(TESTED_FILE, FIRST_NAME_VAR)
    expected = f"Hello, {first_name}!"

    assert (
        printed_output == expected
    ), f"Failed. '{RESULT_VAR}' should be printed out. {printed_output} != {expected}"


def test_greeting_should_not_be_hardcoded():
    first_name = getattr(TESTED_FILE, FIRST_NAME_VAR)

    with open(TESTED_FILE.__file__) as f:
        code = f.read()

        assignment_regex = f"['\"]Hello, {first_name}!['\"]"
        assert (
            re.search(assignment_regex, code) is None
        ), f"Variable '{RESULT_VAR}' should be assigned value using interpolation"


def test_greeting_should_not_be_assigned_using_concatenation():
    with open(TESTED_FILE.__file__) as f:
        code = f.read()

        assignment_regex = r"\+"
        assert (
            re.search(assignment_regex, code) is None
        ), "Variable '{RESULT_VAR}' should be assigned value using interpolation"
