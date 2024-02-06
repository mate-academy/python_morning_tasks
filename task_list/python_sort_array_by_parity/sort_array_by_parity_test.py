from sort_array_by_parity import sort_array_by_parity


def parity_checker(num_list: list[int], parity: str) -> bool:
    match parity:
        case "odd":
            return all([num % 2 for num in num_list])
        case "even":
            return all([num % 2 == 0 for num in num_list])


def test_single_element():
    nums = [5]
    assert (
        result := sort_array_by_parity(nums)
    ) == nums, f"Failed: Result list should be the same as input one for nums = {nums}. Output: {result}"


def test_base_case():
    nums, evens = [3, 1, 2, 4], 2
    result = sort_array_by_parity(nums)
    assert all(
        [parity_checker(result[:evens], "even"), parity_checker(result[evens:], "odd")]
    ), f"Failed: Even numbers should be followed by odd for nums = {nums}. Output: {result}"


def test_only_even_numbers():
    nums, evens = [16, 2, 4, 6, 8, 10, 12], 7
    result = sort_array_by_parity(nums)
    assert (
        parity_checker(result, "even") is True and len(result) == evens
    ), f"Failed: Result list should contain all numbers from input list. Output: {result}"


def test_only_odd_numbers():
    nums, ods = [num for num in range(1, 16, 2)], 8
    result = sort_array_by_parity(nums)

    assert (
        parity_checker(result, "odd") is True and len(result) == ods
    ), f"Failed: Result list should contain all numbers from input list. Output: {result}"


def test_zero_treats_as_even():
    nums = [0, 19, 3, 18, 47, 11, 24]
    evens = 3
    result = sort_array_by_parity(nums)
    assert all(
        [
            parity_checker(result[:evens], "even") is True,
            parity_checker(result[evens:], "odd") is True,
        ]
    ), f"Failed: Even numbers should be followed by odd ones. Output: {result}"

    assert (
        0 in result[:evens]
    ), f"Failed: Zero should be treated as even number for nums = {nums}"
