def smallest_range(nums: list[int], k: int) -> int:
    max_value = max(nums) - k
    min_value = min(nums) + k

    return max_value - min_value if max_value > min_value else 0
