from x_of_a_kind_in_a_deck_of_cards import has_groups_size_x

def test_basic_true_case():
    deck = [1,2,3,4,4,3,2,1]
    assert (
        has_groups_size_x(deck) == True
    ), "Test failed: Expected True for input [1,2,3,4,4,3,2,1]"


def test_basic_false_case():
    deck = [1,1,1,2,2,2,3,3]
    assert (
        has_groups_size_x(deck) == False
    ), "Test failed: Expected True for input [1,1,1,2,2,2,3,3]"


def test_single_card():
    deck = [5]
    assert (
        has_groups_size_x(deck) == False
    ), "Test failed: Expected False for a deck with a single card"


def test_two_identical_cards():
    deck = [7, 7]
    assert (
        has_groups_size_x(deck) == True
    ), "Test failed: Expected True for a deck with two identical cards"


def test_two_different_cards():
    deck = [7, 8]
    assert (
        has_groups_size_x(deck) == False
    ), "Test failed: Expected False for a deck with two different cards"
