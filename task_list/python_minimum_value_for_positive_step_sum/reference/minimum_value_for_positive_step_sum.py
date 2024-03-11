def min_start_value(nums: list[int]) -> int:
    initial_sum, min_value = 0, 1

    for num in nums:
        initial_sum += num
        min_value = max(min_value, 1 - initial_sum)

    return min_value
