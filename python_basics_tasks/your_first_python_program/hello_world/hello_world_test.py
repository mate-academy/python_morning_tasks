import sys

from io import StringIO


def test_hello_world_printed():
    expected_output = "Hello, world!"

    captured_output = StringIO()
    sys.stdout = captured_output

    exec(open("hello_world.py").read())
    printed_output = captured_output.getvalue().strip()
    sys.stdout = sys.__stdout__

    assert (
        printed_output == expected_output
    ), f"Failed. Printed phrase is not valid. Printed: {printed_output}, while Expected: {expected_output}"
