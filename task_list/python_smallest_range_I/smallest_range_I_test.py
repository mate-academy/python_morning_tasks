from smallest_range_I import smallest_range


def test_single_element():
    nums, range_limit = [4], 2
    assert (
        smallest_range(nums, range_limit) == 0
    ), f"Failed: The score should be 0 for nums = {nums} and range_limit = {range_limit}"


def test_max_minus_min_when_limit_is_set_to_zero():
    nums, range_limit = [5, 10, 4, 8, 2], 0
    assert (
        smallest_range(nums, range_limit) == 8
    ), f"Failed: The score should be 10 - 2 = 8 for nums = {nums} and range_limit = {range_limit}"

    nums, range_limit = [124, 224, 150, 198, 125], 0
    assert (
        smallest_range(nums, range_limit) == 100
    ), f"Failed: The score should be 224 - 124 = 100 for nums = {nums} and range_limit = {range_limit}"


def test_negative_numbers_in_list():
    nums, range_limit = [-5, -2, -8, -1], 3
    assert (
        smallest_range(nums, range_limit) == 1
    ), f"Failed: The score should be 1 for nums = {nums} and range_limit = {range_limit}"

    nums, range_limit = [-10, -5, 0, -3, -8], 2
    assert (
        smallest_range(nums, range_limit) == 6
    ), f"Failed: The score should be 6 for nums = {nums} and range_limit = {range_limit}"


def test_large_nums_size():
    nums = list(range(1, 10**3 + 1))
    range_limit = 450
    assert (
        smallest_range(nums, range_limit) == 99
    ), f"Failed: The score should be 99 for nums = {nums} and range_limit = {range_limit}"


def test_limit_greater_than_max_value():
    nums, range_limit = [1, 2, 3], 4
    assert (
        smallest_range(nums, range_limit) == 0
    ), f"Failed: The score should be 0 for nums = {nums} and range_limit = {range_limit}"
