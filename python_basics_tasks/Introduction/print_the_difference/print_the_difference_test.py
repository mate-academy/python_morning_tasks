import sys

from io import StringIO


def test_difference_equals_3_and_was_printed():
    captured_output = StringIO()
    sys.stdout = captured_output

    exec(open("print_the_difference.py").read())
    printed_output = captured_output.getvalue().strip()
    sys.stdout = sys.__stdout__

    assert (
        int(printed_output) == 3
    ), f"The difference that equals to {3} should be printed. Printed: {printed_output}"
