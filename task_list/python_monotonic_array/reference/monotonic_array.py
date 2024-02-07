def is_monotonic(nums: list[int]) -> bool:
    increasing = True
    decreasing = True

    for idx in range(1, len(nums)):
        if nums[idx] < nums[idx - 1]:
            increasing = False
        elif nums[idx] > nums[idx - 1]:
            decreasing = False

        if not increasing and not decreasing:
            break

    return increasing or decreasing
