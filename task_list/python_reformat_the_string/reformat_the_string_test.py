from reformat_the_string import reformat_string


def assert_message(input_data: str, output: str, solutions: list[str] = None) -> str:
    msg = "Should be empty string returned"
    if solutions is not None:
        possible_solutions = ", ".join(solutions)
        msg = f"Returned result should be among these possible solutions: ({possible_solutions})"
    return f"Failed. {msg}. Output: {output}"


def test_base_cases():
    input_data = "a0b1c2"
    solutions = ["2c1b0a", "0a1b2c", "0a1b2c", "0c2a1b"]
    result = reformat_string(input_data)
    assert result in solutions, assert_message(input_data, result, solutions)

    input_data = "leetcode"
    solution = ""
    result = reformat_string(input_data)
    assert result == solution, assert_message(input_data, result)

    input_data = "1229857369"
    solution = ""
    result = reformat_string(input_data)
    assert result == solution, assert_message(input_data, result)


def test_same_consecutive_chars_should_be_separated():
    input_data = "ab123"
    solutions = [
        "1a2b3",
        "1a3b2",
        "1b2a3",
        "1b3a2" "2a1b3",
        "2a3b1",
        "2b1a3",
        "2b3a1" "3a1b2",
        "3a2b1",
        "3b1a2",
        "3b2a1",
    ]
    result = reformat_string(input_data)
    assert result in solutions, assert_message(input_data, result, solutions)

    input_data = "12xy"
    solutions = ["1x2y", "1y2x", "2x1y", "2y1x", "x1y2", "x2y1" "y1x2", "y2x1"]
    result = reformat_string(input_data)
    assert result in solutions, assert_message(input_data, result, solutions)


def test_input_data_as_valid_solution():
    input_data = "x1"
    solutions = ["x1", "1x"]
    result = reformat_string(input_data)
    assert result in solutions, assert_message(input_data, result, solutions)

    input_data = "x1y"
    solutions = ["x1y", "y1x"]
    result = reformat_string(input_data)
    assert result in solutions, assert_message(input_data, result, solutions)
