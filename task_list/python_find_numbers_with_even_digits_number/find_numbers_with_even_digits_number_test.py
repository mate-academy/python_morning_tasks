from find_numbers_with_even_digits_number import find_numbers


def assert_message(input_data: list[int], expected: int, output: int) -> str:
    return f"Failed. For list={input_data} correct answert is equal to {expected}. Your output: {output}"


def test_base_cases():
    input_data = [12, 345, 2, 6, 7896]
    expected = 2
    output = find_numbers(input_data)
    assert output == expected, assert_message(input_data, expected, output)

    input_data = [555, 901, 482, 1771]
    expected = 1
    output = find_numbers(input_data)
    assert output == expected, assert_message(input_data, expected, output)


def test_single_digit_numbers():
    input_data = [1, 2, 3, 4, 5]
    expected = 0
    output = find_numbers(input_data)
    assert output == expected, assert_message(input_data, expected, output)


def test_large_numbers():
    input_data = [10**num for num in range(2, 6)]
    expected = 2
    output = find_numbers(input_data)
    assert output == expected, assert_message(input_data, expected, output)

    input_data = [10**3] * 5 + [10**4] * 3
    expected = 5
    output = find_numbers(input_data)
    assert output == expected, assert_message(input_data, expected, output)


def test_large_lists():
    three_digits = [num for num in range(101, 123)]
    five_digits = [num for num in range(11788, 12001)]
    even_digits = [10**3] * 3 + [10**5] * 7
    input_data = three_digits + even_digits + five_digits
    expected = 10
    output = find_numbers(input_data)
    assert output == expected, assert_message(input_data, expected, output)
