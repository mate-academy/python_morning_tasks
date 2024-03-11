def find_distance_value(
    first_list: list[int], second_list: list[int], target: int
) -> int:
    """
    More complicated but also more efficient solution. Something like binary search approach
    """

    second_list.sort()
    count = 0

    first_len, second_len = len(first_list), len(second_list)

    for num in range(first_len):
        low, high = 0, second_len - 1

        while low <= high:
            mid = (low + high) // 2

            if abs(first_list[num] - second_list[mid]) <= target:
                count += 1
                break
            elif first_list[num] < second_list[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return first_len - count
