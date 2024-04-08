import subprocess
import ast
import random

import turn_into_list


expected_range = range(1, 251)
expected_list = list(expected_range)
expected_len = len(expected_list)


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
    res = collection[start:end]
    return res


def test_valid_list_printed():
    process = subprocess.Popen(
        ["python", turn_into_list.__file__], stdout=subprocess.PIPE
    )

    captured_output_str = process.communicate()[0].decode()
    assert (
        captured_output_str
    ), "Failed. Result list should be printed out using 'print()' function."

    printed_output_raw = ast.literal_eval(captured_output_str)
    assert (
        len(printed_output_raw) == expected_len
    ), f"Failed. Printed list's length should be {expected_len}. {len(printed_output_raw)} != {expected_len}"

    compare: list = generate_pairs(5, expected_list, printed_output_raw)
    assert (
        all(compare) is True
    ), f"Failed. Printed list should be valid and contain numbers in range {expected_range}"
