from reference.sort_list_by_parity_ll import sort_list_by_parity


def test_with_mixed_even_and_odd_numbers():
    assert all(
        num % 2 == i % 2 for i, num in enumerate(sort_list_by_parity([4, 2, 5, 7]))
    ), "Even and odd indices should match the parity of numbers."


def test_with_already_sorted_list():
    assert all(
        num % 2 == i % 2 for i, num in enumerate(sort_list_by_parity([2, 3]))
    ), "Even and odd indices should match the parity of numbers."


def test_with_multiple_even_and_odd_numbers():
    assert all(
        num % 2 == i % 2
        for i, num in enumerate(sort_list_by_parity([2, 4, 6, 1, 3, 5]))
    ), "Even and odd indices should match the parity of numbers."


def test_with_all_even_followed_by_odd():
    assert all(
        num % 2 == i % 2
        for i, num in enumerate(sort_list_by_parity([2, 4, 6, 8, 1, 3, 5, 7]))
    ), "Even and odd indices should match the parity of numbers."


def test_with_all_odd_followed_by_even():
    assert all(
        num % 2 == i % 2
        for i, num in enumerate(sort_list_by_parity([1, 3, 5, 7, 2, 4, 6, 8]))
    ), "Even and odd indices should match the parity of numbers."


def test_with_empty_list():
    assert sort_list_by_parity([]) == [], "Empty list should return an empty list."
