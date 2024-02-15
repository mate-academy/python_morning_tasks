# Time complexity: O(n)

# Space: The space complexity of this function is O(n),
# where n is the number of unique elements in the input list nums.
# This is because we use a hashmap to store the frequency of each element,
# and a set to store unique elems. Both sizes are at most "n"


def find_lucky(nums: list[int]) -> int:
    lucky_number = -1

    hashmap = {}
    for num in nums:
        if num in hashmap:
            hashmap[num] += 1
            continue
        hashmap[num] = 1

    unique_nums = set(nums)

    for elem in unique_nums:
        if not hashmap[elem] == elem:
            continue
        if elem > lucky_number:
            lucky_number = elem
    return lucky_number
