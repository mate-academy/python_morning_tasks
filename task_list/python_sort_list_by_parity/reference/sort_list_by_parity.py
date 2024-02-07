def sort_list_by_parity(nums: list[int]) -> list[int]:
    pointer = 0

    for idx, value in enumerate(nums):
        if value % 2 == 0:
            nums[pointer], nums[idx] = nums[idx], nums[pointer]
            pointer += 1

    return nums
