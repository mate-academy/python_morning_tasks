from monotonic_list import is_monotonic


def assert_message(nums: list[int], expected: bool, output: bool) -> str:
    return f"Failed: Should be returned {expected} for list = {nums}. Output: {output}"


def test_base_cases():
    nums = [1, 2, 2, 3]
    expected = True
    result = is_monotonic(nums)
    assert result == expected, assert_message(nums, expected, result)

    nums = [6, 5, 4, 4]
    expected = True
    result = is_monotonic(nums)
    assert result == expected, assert_message(nums, expected, result)

    nums = [1, 3, 2]
    expected = False
    result = is_monotonic(nums)
    assert result == expected, assert_message(nums, expected, result)


def test_single_value_in_list():
    nums = [5]
    expected = True
    result = is_monotonic(nums)
    assert result == expected, assert_message(nums, expected, result)


def test_all_elements_are_the_same():
    nums = [3, 3, 3, 3, 3]
    expected = True
    result = is_monotonic(nums)
    assert result == expected, assert_message(nums, expected, result)

    nums = [0, 0, 0, 0, 0]
    expected = True
    result = is_monotonic(nums)
    assert result == expected, assert_message(nums, expected, result)


def test_negative_numbers_in_list():
    nums = [-5, -4, -3, -2, -1]
    expected = True
    result = is_monotonic(nums)
    assert result == expected, assert_message(nums, expected, result)

    nums = [1, -2, 3, -4, 5]
    expected = False
    result = is_monotonic(nums)
    assert result == expected, assert_message(nums, expected, result)


def test_random_order_cases():
    nums = [2, 4, 1, 3, 5]
    expected = False
    result = is_monotonic(nums)
    assert result == expected, assert_message(nums, expected, result)

    nums = [1, 2, 3, 3, 4, 5, 5, 5, 4, 6, 7]
    expected = False
    result = is_monotonic(nums)
    assert result == expected, assert_message(nums, expected, result)

    nums = [-5, -5, 0, 4, 7, -8, 9, -10]
    expected = False
    result = is_monotonic(nums)
    assert result == expected, assert_message(nums, expected, result)
