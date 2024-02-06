def smallest_range(nums: list[int], range_limit: int) -> int:
    max_value = max(nums) - range_limit
    min_value = min(nums) + range_limit

    return max_value - min_value if max_value > min_value else 0
