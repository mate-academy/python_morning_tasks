# Solution #2. O(n) with self-written common divisor. 
def has_groups_size_x(deck: list[int]) -> bool:
    card_counts = {}
    for card in deck:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1

    def find_gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_val = card_counts[deck[0]]

    for count in card_counts.values():
        gcd_val = find_gcd(gcd_val, count)

    return gcd_val > 1
