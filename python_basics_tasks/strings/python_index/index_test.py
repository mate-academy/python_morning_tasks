import re
import subprocess

import index


TESTED_FILE = index
VAR_NAME = "goal"
VAR_VALUE = "Help 1 million people worldwide build their careers in Tech."


def test_variable_is_defined():
    assert hasattr(
        TESTED_FILE, VAR_NAME
    ), f"Failed. Variable '{VAR_NAME}' should be defined"

    result_value = getattr(TESTED_FILE, VAR_NAME)
    assert (
        result_value == VAR_VALUE
    ), f"Failed. ( {VAR_VALUE} ) should be stored in the '{VAR_NAME}' variable"


def test_printed_variable_with_index():
    with open(TESTED_FILE.__file__) as f:
        file_content = f.read()

        pattern = r"print\(goal\[5\]\)"
        regex_search = re.search(pattern, file_content)
        assert (
            regex_search
        ), f"Failed. Variable '{VAR_NAME}' with proper index should be printed"
