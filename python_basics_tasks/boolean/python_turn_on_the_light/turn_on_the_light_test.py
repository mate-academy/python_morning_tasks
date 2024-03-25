import re
import subprocess

import turn_on_the_light


TESTED_FILE = turn_on_the_light
VAR_NAME = "is_light_on"
VAR_VALUE = True


def test_variable_is_defined_and_not_changed():
    assert hasattr(
        TESTED_FILE, VAR_NAME
    ), f"Failed. Variable {VAR_NAME} should be defined"

    variable = getattr(TESTED_FILE, VAR_NAME)

    assert isinstance(
        variable, bool
    ), f"Failed. Variable {VAR_NAME} should be <bool> type"
    assert (
        variable == VAR_VALUE
    ), f"Failed. Variable {VAR_NAME} should be equal to {VAR_VALUE}. {variable} != {VAR_VALUE}"


def test_expected_result_was_printed():
    process = subprocess.Popen(
        ["python", turn_on_the_light.__file__], stdout=subprocess.PIPE
    )

    captured_output = process.communicate()[0].decode()
    printed_output = captured_output.strip()

    expected = not VAR_VALUE

    assert printed_output == str(
        expected
    ), f"Failed. '{expected}' should be printed out. {printed_output} != {expected}"


def test_result_not_hardcoded():
    with open(TESTED_FILE.__file__) as file:
        code = file.read()

        pattern = r"\bFalse\b"
        assert (
            re.search(pattern, code) is None
        ), "Failed. You should not hardcode 'False' to pass the tests"


def test_result_printed_with_not():
    with open(TESTED_FILE.__file__) as file:
        code = file.read()

        pattern = r"print\(not is_light_on\)"
        assert (
            re.search(pattern, code) is not None
        ), "Failed. You shoud use <print()> and <not> to print out result"
