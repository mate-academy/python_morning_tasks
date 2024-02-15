# Time complexity: O(n^2 + nlog(n)) => O(n^2)
# Space: O(n)
def find_lucky(nums: list[int]) -> int:
    counter = 0
    result = []

    for num_idx in range(len(nums)):
        if nums.count(nums[num_idx]) == nums[num_idx]:
            counter += 1
            result.append(nums[num_idx])
    if counter == 0:
        return -1
    result.sort()
    return result[-1]
