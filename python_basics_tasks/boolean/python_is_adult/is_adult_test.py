import re
import subprocess
import ast

import is_adult


TEST_FILE = is_adult
AGE_VAR_NAME = "age"
BOOL_VAR_NAME = "is_adult"


def test_variables_are_defined():
    assert hasattr(
        TEST_FILE, AGE_VAR_NAME
    ), f"Failed. Variable '{AGE_VAR_NAME}' should be defined"
    assert hasattr(
        TEST_FILE, BOOL_VAR_NAME
    ), f"Failed. Do not remove '{BOOL_VAR_NAME}' variable"

    age_value = getattr(TEST_FILE, AGE_VAR_NAME)
    bool_var_value = getattr(TEST_FILE, BOOL_VAR_NAME)

    assert isinstance(
        age_value, int
    ), f"Failed. Variable '{AGE_VAR_NAME}' should be <int> type"
    assert isinstance(
        bool_var_value, bool
    ), f"Failed. Variable '{BOOL_VAR_NAME}' should be <bool> type"


def test_no_hardcoded_booleans():
    with open(TEST_FILE.__file__) as f:
        content = f.read()
        pattern = r"\b(?:True|False)\b"
        assert (
            re.search(pattern, content) is None
        ), f"Failed. '{is_adult}' variable should be used to store boolean. No hardcoded values are allowed."


def test_bool_was_printed():
    age_value = getattr(TEST_FILE, AGE_VAR_NAME)
    expected_bool = age_value <= 18

    process = subprocess.Popen(["python", "is_adult.py"], stdout=subprocess.PIPE)
    captured_string_output = process.communicate()[0].decode()
    assert (
        captured_string_output
    ), f"Failed. Result should be printed out with 'print()' function"

    printed_output_raw = ast.literal_eval(captured_string_output)
    assert (
        printed_output_raw is expected_bool
    ), f"Failed. {printed_output_raw} != {expected_bool}"
