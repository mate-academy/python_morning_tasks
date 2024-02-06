from collections import Counter
from math import gcd


def has_groups_size_x(deck: list[int]) -> bool:
    card_counts = Counter(deck)

    gcd_val = 0
    for count in card_counts.values():
        gcd_val = gcd(gcd_val, count)

    return gcd_val > 1
