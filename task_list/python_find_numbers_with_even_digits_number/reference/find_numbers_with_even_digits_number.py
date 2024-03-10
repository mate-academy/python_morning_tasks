from math import floor, log10


def find_numbers(nums: list[int]) -> int:
    result = 0

    for num in nums:
        digits = floor(log10(num)) + 1
        if digits % 2 == 0:
            result += 1
    return result
