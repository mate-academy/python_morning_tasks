def find_distance_value(
    first_list: list[int], second_list: list[int], target: int
) -> int:
    """
    Simple and straightforward solution ( brute force ).
    """

    counter = 0

    for first_num in first_list:
        for second_num in second_list:
            diff = abs(first_num - second_num)
            if diff <= target:
                counter += 1
                break

    return len(first_list) - counter
