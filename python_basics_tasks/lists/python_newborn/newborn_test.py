import subprocess
import ast
import re

import newborn

TEST_FILE = newborn
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
        len(result_value) >= 2
    ), f"Failed. '{VAR_NAME}' should contain one more name in addition to previous list"


def test_family_members_printed():
    result_value = getattr(TEST_FILE, VAR_NAME)

    process = subprocess.Popen(["python", newborn.__file__], stdout=subprocess.PIPE)
    captured_string_output = process.communicate()[0].decode()
    assert (
        captured_string_output
    ), "Failed. Your family list should be printed with 'print()' function."

    printed_output_raw = ast.literal_eval(captured_string_output)
    assert (
        printed_output_raw == result_value
    ), f"Failed. Proper '{VAR_NAME}' should be printed. {printed_output_raw} != {result_value}"


def test_additional_name_added_with_append():
    with open(TEST_FILE.__file__) as f:
        code = f.read()

        pattern = r"my_family\.append\((?:'[^']*'|\"[^\"]*\")\)"
        assert (
            re.search(pattern, code) is not None
        ), "Failed. Additionl name to a list should be added using <append> method and not hardcoded."
