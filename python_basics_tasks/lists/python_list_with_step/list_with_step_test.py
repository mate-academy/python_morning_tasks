import subprocess
import ast
import re
import random

import list_with_step


expected_range = range(1, 251)
expected_odd_list = [num for num in expected_range if num % 2 == 1]
expected_len = len(expected_odd_list)


def generate_pairs(pairs_num: int, expected: list, actual: list) -> list:
    result_list = []
    for num in range(pairs_num):
        start, end = random.choice(expected_range), random.choice(expected_range)
        if num % 3 == 0:
            start *= -1

        first = take_slice(expected, start, end)
        second = take_slice(actual, start, end)
        result_list.append(first == second)

    return result_list


def take_slice(collection: list, start: int, end: int) -> list:
    return collection[start:end]


def test_odd_numbers_generated_via_slice():
    with open(list_with_step.__file__) as file:
        code = file.read()

        pattern = r"\[(\d*):(\d*):(\d+)\]"
        match = re.search(pattern, code)

        assert (
            match is not None
        ), "Failed. Odd books pages should be generated using slice with step"

        start, stop, step = match.group(1), match.group(2), match.group(3)
        compare = [
            any([start == "", start == "0"]),
            any([stop == "", stop == "251"]),
            step == "2",
        ]
        assert (
            all(compare) is True
        ), f"Failed. Your slice: {match.group()} is not valid in terms of getting odd book pages"


def test_valid_list_printed():
    process = subprocess.Popen(
        ["python", list_with_step.__file__], stdout=subprocess.PIPE
    )

    captured_output_str = process.communicate()[0].decode()
    assert (
        captured_output_str
    ), "Failed. Result list should be printed out using 'print()' function."

    printed_output_raw = ast.literal_eval(captured_output_str)
    assert isinstance(
        printed_output_raw, list
    ), "Failed. Printed result should be of type <list>"
    assert (
        len(printed_output_raw) == expected_len
    ), f"Failed. Printed list's length should be {expected_len}. {len(printed_output_raw)} != {expected_len}"

    compare: list = generate_pairs(12, expected_odd_list, printed_output_raw)
    assert (
        all(compare) is True
    ), f"Failed. Printed list should be valid and contain only odd numbers in range {expected_range}"
