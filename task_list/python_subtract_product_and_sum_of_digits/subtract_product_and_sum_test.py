from subtract_product_and_sum import subtract_product_and_sum


def assert_message(input_num: int, expected: int, output: int) -> str:
    return f"Failed. For num={input_num} valid result equals={expected}. Your output: {output}"


def test_base_cases():
    input_data = 234
    expected = 15
    result = subtract_product_and_sum(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = 4421
    expected = 21
    result = subtract_product_and_sum(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_edge_numbers():
    input_data = 1
    expected = 0
    result = subtract_product_and_sum(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = 99999
    expected = 59004
    result = subtract_product_and_sum(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_with_negative_answer():
    input_data = 1908
    expected = -18
    result = subtract_product_and_sum(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = 88990
    expected = -34
    result = subtract_product_and_sum(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = 190
    expected = -10
    result = subtract_product_and_sum(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_random_big_numbers():
    input_data = 12345
    expected = 105
    result = subtract_product_and_sum(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = 7771
    expected = 321
    result = subtract_product_and_sum(input_data)
    assert result == expected, assert_message(input_data, expected, result)
