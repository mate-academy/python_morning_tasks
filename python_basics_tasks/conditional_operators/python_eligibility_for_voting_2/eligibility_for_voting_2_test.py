import subprocess

import eligibility_for_voting_2


TESTED_FILE = eligibility_for_voting_2
VAR_NAME = "person_age"
VAR_VALUE = 15
PHRASE_TO_PRINT = "You cannot vote"


def test_variable_is_properly_defined():
    assert hasattr(
        TESTED_FILE, VAR_NAME
    ), f"Failed. Variable '{VAR_NAME}' should be defined."

    age = getattr(TESTED_FILE, VAR_NAME)

    assert isinstance(age, int), f"Failed. '{VAR_NAME}' should be type <int>."
    assert (
        age == VAR_VALUE
    ), f"Failed. '{VAR_NAME}' should be equal to <{VAR_VALUE}>. '{VAR_VALUE} != {age}'."


def test_print_works_correctly():
    process = subprocess.Popen(["python", TESTED_FILE.__file__], stdout=subprocess.PIPE)
    captured_print = process.communicate()[0].decode().strip()

    assert (
        captured_print
    ), "Failed. Result should be printed out with 'print()' function"

    assert (
        captured_print == PHRASE_TO_PRINT
    ), f"Failed. {PHRASE_TO_PRINT} should be printed. Your output: '{captured_print}'"
