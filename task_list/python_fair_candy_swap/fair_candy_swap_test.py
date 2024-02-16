import random


import pytest


from fair_candy_swap import candy_swap


def generate_constant_candy_amount(sizes_sum: int) -> tuple[list, list]:
    candies1 = [1 for _ in range(sizes_sum)]
    candies2 = [2 for _ in range(sizes_sum)]
    return candies1 + [3], candies2 + [sizes_sum + 3]


def generate_unique_boxes(sizes_sum: int) -> tuple[list, list]:
    candies1 = [box for box in range(1, sizes_sum) if box % 2 == 1]
    candies2 = [box for box in range(1, sizes_sum + 1) if box % 2 == 0]
    return candies1 + [sizes_sum + 5], candies2 + [5]


def generate_different_box_amount(sizes_sum: int) -> tuple[list, list]:
    chunk = sizes_sum // 100
    candies1 = [box for box in range(1, sizes_sum)]
    candies2 = [box for box in range(chunk, sizes_sum)]
    return candies1, candies2


def generate_single_box_vs_large_list(sizes_sum: int) -> tuple[list, list]:
    single_box = random.randint(sizes_sum // 10, sizes_sum // 2)
    candies1 = [single_box]
    candies2 = [1 for box in range(1, sizes_sum) if box % 2]
    total_candies2 = sum(candies2)
    return candies1, candies2 + [total_candies2 + single_box]


generator_mapper = {
    "same_boxes": generate_constant_candy_amount,
    "unique_boxes": generate_unique_boxes,
    "different_sizes": generate_different_box_amount,
    "single_box": generate_single_box_vs_large_list,
}


def assert_message(
    alice: list[int], bob: list[int], expected: list[int], output: list[int]
) -> str:
    return f"Failed: Should return {expected} for following input: alice={alice}, bob={bob}. Output: {output}"


def test_base_cases():
    input_data = ([1, 1], [2, 2])
    expected = [1, 2]
    result = candy_swap(*input_data)
    assert result == expected, assert_message(
        *input_data, expected=expected, output=result
    )

    input_data = ([1, 2], [2, 3])
    expected = [1, 2]
    result = candy_swap(*input_data)
    assert result == expected, assert_message(
        *input_data, expected=expected, output=result
    )

    input_data = ([2], [1, 3])
    expected = [2, 3]
    result = candy_swap(*input_data)
    assert result == expected, assert_message(
        *input_data, expected=expected, output=result
    )


def test_alice_has_more_candies():
    input_data = ([1, 3], [2])
    expected = [3, 2]
    result = candy_swap(*input_data)
    assert result == expected, assert_message(
        *input_data, expected=expected, output=result
    )

    input_data = ([300, 200, 40, 60], [100, 55, 45])
    expected = [300, 100]
    result = candy_swap(*input_data)
    assert result == expected, assert_message(
        *input_data, expected=expected, output=result
    )

    input_data = ([10, 5, 2], [3])
    expected = [10, 3]
    result = candy_swap(*input_data)
    assert result == expected, assert_message(
        *input_data, expected=expected, output=result
    )


def test_random_box_configurations():
    cases = ["unique_boxes", "single_box", "different_sizes", "same_boxes"]

    for case in cases:
        sum_sizes = random.randint(100, 10000)
        gen_func = generator_mapper[case]
        alice_candies, bob_candies = gen_func(sum_sizes)
        result = candy_swap(alice_candies, bob_candies)

        assert isinstance(result, list), "Failed: Should return a list"
        assert len(result) == 2, "Failed: Alice and Bob should swap with boxes"
        alice_gift, bob_gift = result
        assert (
            sum(alice_candies) - alice_gift + bob_gift
            == sum(bob_candies) - bob_gift + alice_gift
        ), "Failed: After Alice and Bob have swapped boxes the total amount of candies should be equal"
        assert all(
            [alice_gift in set(alice_candies), bob_gift in set(bob_candies)]
        ), "Failed: Variability of boxes Alice and Bob can swap is determined by corresponding lists"
