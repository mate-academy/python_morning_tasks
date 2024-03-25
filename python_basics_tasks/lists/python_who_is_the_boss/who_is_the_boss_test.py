import subprocess
import re

import who_is_the_boss

TEST_FILE = who_is_the_boss
VAR_NAME = "my_family"


def test_variables_defined():
    assert hasattr(
        TEST_FILE, VAR_NAME
    ), f"Failed. Variable '{VAR_NAME}' should be defined"

    result_value = getattr(TEST_FILE, VAR_NAME)
    assert isinstance(
        result_value, list
    ), f"Failed. Variable '{VAR_NAME}' should be <list> type"
    assert (
        len(result_value) >= 1
    ), f"Failed. '{VAR_NAME}' should contain at least one name of your family member"


def test_first_family_members_printed():
    result_value = getattr(TEST_FILE, VAR_NAME)[0]

    process = subprocess.Popen(["python", "who_is_the_boss.py"], stdout=subprocess.PIPE)
    captured_output = process.communicate()[0].decode().strip()
    assert (
        captured_output
    ), "Failed. Your family list should be printed with 'print()' function."

    assert (
        captured_output == result_value
    ), f"Failed. Proper '{VAR_NAME}' should be printed. {captured_output} != {result_value}"


def test_first_family_member_not_hardcoded_in_print():
    with open(TEST_FILE.__file__) as file:
        code = file.read()

        pattern = r"print\(my_family\[0\]\)"
        assert (
            re.search(pattern, code) is not None
        ), "Failed. First family member should be printed out using index and not hardcoded."
