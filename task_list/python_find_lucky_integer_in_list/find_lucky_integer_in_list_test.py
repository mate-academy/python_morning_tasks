from find_lucky_integer_in_list import find_lucky


def assert_message(nums: list[int], expected: int, output: int) -> str:
    return f"Failed: Should return {expected} for nums={nums}. Output: {output}"


def test_base_cases():
    nums = [2, 2, 3, 4]
    expected = 2
    result = find_lucky(nums)
    assert result == expected, assert_message(nums, expected, result)

    nums = [1, 2, 2, 3, 3, 3]
    expected = 3
    result = find_lucky(nums)
    assert result == expected, assert_message(nums, expected, result)

    nums = [2, 2, 2, 3, 3]
    expected = -1
    result = find_lucky(nums)
    assert result == expected, assert_message(nums, expected, result)


def test_single_element_list():
    nums = [5]
    expected = -1
    result = find_lucky(nums)
    assert result == expected, assert_message(nums, expected, result)


def test_same_elements():
    nums = [4, 4, 4, 4]
    expected = 4
    result = find_lucky(nums)
    assert result == expected, assert_message(nums, expected, result)

    nums = [5, 5, 5, 5]
    expected = -1
    result = find_lucky(nums)
    assert result == expected, assert_message(nums, expected, result)


def test_large_scale_frequencies():
    additional_nums = [17, 244, 11, 2, 2, 3, 3, 3, 15, 67]

    nums = [num if num % 2 else 16 for num in range(23, 55)] + additional_nums
    expected = 16
    result = find_lucky(nums)
    assert result == expected, assert_message(nums, expected, result)

    nums = [500] * 500 + additional_nums
    expected = 500
    result = find_lucky(nums)
    assert result == expected, assert_message(nums, expected, result)

    nums = [300] * 299 + additional_nums
    expected = -1
    result = find_lucky(nums)
    assert result == expected, assert_message(nums, expected, result)
