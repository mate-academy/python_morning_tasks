def sort_array_by_parity(nums: list[int]) -> list[int]:
    even_nums = [num for num in nums if num % 2 == 0]
    odd_nums = [num for num in nums if num % 2 != 0]

    result = []
    for even, odd in zip(even_nums, odd_nums):
        result.extend([even, odd])

    return result
