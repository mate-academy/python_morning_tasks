from minimum_subsequence_sum import min_subsequence


def assert_message(
    input_list: list[int], expected: list[int], output: list[int]
) -> str:
    return f"Failed. For list={input_list} valid answer equals={expected}. Your output: {output}"


def test_base_cases():
    input_data = [4, 3, 10, 9, 8]
    expected = [10, 9]
    result = min_subsequence(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = [4, 4, 7, 6, 7]
    expected = [7, 7, 6]
    result = min_subsequence(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_smallest_possible_lists():
    input_data = [13]
    expected = [13]
    result = min_subsequence(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = [5, 6]
    expected = [6]
    result = min_subsequence(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_maximum_length():
    max_number = 500
    input_data = [100] * max_number
    expected_len = 251
    expected_sum = 25100
    result = min_subsequence(input_data)
    assert (
        len(result) == expected_len
    ), f"Failed for list with {max_number} of elements. Should return list with {expected_len} elems"
    assert (
        sum(result) == expected_sum
    ), f"Failed for lisst with {max_number} of elements. The sum of returned list should equal {expected_sum}"
