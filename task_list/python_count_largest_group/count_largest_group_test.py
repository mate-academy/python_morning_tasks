from count_largest_group import count_largest_group


def assert_message(input_number: int, expected: int, output: int) -> str:
    return f"Failed. For number={input_number} amount of largest groups is {expected}, while you returned {output}"


def test_base_cases():
    input_data = 13
    expected = 4
    result = count_largest_group(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = 2
    expected = 2
    result = count_largest_group(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_edge_numbers():
    input_data = 1
    expected = 1
    result = count_largest_group(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = 10**4
    expected = 1
    result = count_largest_group(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = 999
    expected = 2
    result = count_largest_group(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_with_big_amount_of_groups():
    input_data = 37
    expected = 7
    result = count_largest_group(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = 8
    expected = 8
    result = count_largest_group(input_data)
    assert result == expected, assert_message(input_data, expected, result)
