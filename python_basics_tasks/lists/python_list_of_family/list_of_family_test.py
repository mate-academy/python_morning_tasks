import subprocess
import ast

import list_of_family

TEST_FILE = list_of_family
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


def test_family_members_printed():
    result_value = getattr(TEST_FILE, VAR_NAME)

    process = subprocess.Popen(["python", "list_of_family.py"], stdout=subprocess.PIPE)
    captured_string_output = process.communicate()[0].decode()
    assert (
        captured_string_output
    ), "Failed. Your family list should be printed with 'print()' function."

    printed_output_raw = ast.literal_eval(captured_string_output)
    assert (
        printed_output_raw == result_value
    ), f"Failed. Proper '{VAR_NAME}' should be printed. {printed_output_raw} != {result_value}"
