def min_subsequence(nums: list[int]) -> list[int]:
    nums.sort()
    result_list = []

    while sum(result_list) <= sum(nums):
        result_list.append(nums.pop())

    return result_list
