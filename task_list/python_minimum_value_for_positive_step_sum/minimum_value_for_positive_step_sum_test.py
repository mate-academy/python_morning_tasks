from minimum_value_for_positive_step_sum import min_start_value


def assert_message(input_list: list[int], expected: int, output: int) -> str:
    return (
        f"Failed. For list={input_list}, minimu value={expected}. Your output: {output}"
    )


def test_base_case():
    input_data = [-3, 2, -3, 4, 2]
    expected = 5
    result = min_start_value(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = [1, 2]
    expected = 1
    result = min_start_value(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = [1, -2, -3]
    expected = 5
    result = min_start_value(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_all_negative_numbers():
    input_data = [-6] * 5
    expected = 31
    result = min_start_value(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_all_positive_numbers():
    input_data = [15] * 35
    expected = 1
    result = min_start_value(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_maximum_length():
    input_data = [num * -1 if num % 2 == 0 else num for num in range(1, 101)]
    expected = 51
    result = min_start_value(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_max_value():
    input_data = [100, -100]
    expected = 1
    result = min_start_value(input_data)
    assert result == expected, assert_message(input_data, expected, result)
