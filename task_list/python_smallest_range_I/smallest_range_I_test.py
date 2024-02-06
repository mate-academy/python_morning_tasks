from smallest_range_I import smallest_range


def test_single_element():
    nums, k = [4], 2
    assert smallest_range(nums, k) == 0, "Failed: The score should be 0"


def test_max_minus_min_when_k_is_zero():
    nums, k = [5, 10, 4, 8, 2], 0
    assert smallest_range(nums, k) == 8, "Failed: The score should be 10 - 2 = 8"

    nums, k = [124, 224, 150, 198, 125], 0
    assert smallest_range(nums, k) == 100, "Failed: The score should be 224 - 124 = 100"


def test_negative_numbers_in_array():
    nums, k = [-5, -2, -8, -1], 3
    assert smallest_range(nums, k) == 1, "Failed: The score should be 1"

    nums, k = [-10, -5, 0, -3, -8], 2
    assert smallest_range(nums, k) == 6, "Failed: The score should be 6"


def test_large_nums_size():
    nums = list(range(1, 10**3 + 1))
    k = 450
    assert smallest_range(nums, k) == 99, "Failed: The score should be 99"


def test_k_greater_than_max_value():
    nums, k = [1, 2, 3], 4
    assert smallest_range(nums, k) == 0, "Failed: The score should be 0"
