def is_monotonic(nums: list[int]) -> bool:
    increasing = True
    decreasing = True

    for _id in range(1, len(nums)):
        if nums[_id] < nums[_id - 1]:
            increasing = False
        elif nums[_id] > nums[_id - 1]:
            decreasing = False

        if not increasing and not decreasing:
            break

    return increasing or decreasing
