from element_appears_more_than_quarter_of_times import find_integer


def assert_message(input_data: list[int], expected: int, output: int) -> str:
    return f"Failed. For list={input_data} valid answer is {expected}. Your output: {output}"


def test_base_cases():
    input_data = [1, 2, 2, 6, 6, 6, 6, 7, 10]
    expected = 6
    output = find_integer(input_data)
    assert output == expected, assert_message(input_data, expected, output)

    input_data = [1, 1]
    expected = 1
    output = find_integer(input_data)
    assert output == expected, assert_message(input_data, expected, output)


def test_element_appears_exactly_25_percent_times():
    input_data = [17, 2, 45, 1, 3, 99, 12, 45]
    expected = 45
    output = find_integer(input_data)
    assert output == expected, assert_message(input_data, expected, output)

    input_data = [1, 2, 3, 3]
    expected = 3
    output = find_integer(input_data)
    assert output == expected, assert_message(input_data, expected, output)


def test_elements_appear_more_than_25_percent_times():
    input_data = [1, 3, 3, 3, 2, 17, 3, 3, 3]
    expected = 3
    output = find_integer(input_data)
    assert output == expected, assert_message(input_data, expected, output)


def test_single_element():
    input_data = [400]
    expected = 400
    output = find_integer(input_data)
    output = find_integer(input_data)
    assert output == expected, assert_message(input_data, expected, output)


def test_large_list():
    large_list = [num for num in range(15, 1000)]
    repeating_num = [13] * 350
    input_data = large_list + repeating_num
    expected = 13
    output = find_integer(input_data)
    assert output == expected, assert_message(input_data, expected, output)
