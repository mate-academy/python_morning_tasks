# def candy_swap(alice_candies: list[int], bob_candies: list[int]) -> list[int]:
#     pass
def candy_swap(alice_candies: list[int], bob_candies: list[int]) -> list[int]:
    alice_total = sum(alice_candies)
    bob_total = sum(bob_candies)

    target = (alice_total + bob_total) // 2
    bob_set = set(bob_candies)

    for alice_box in alice_candies:
        bob_box = target - (alice_total - alice_box)
        if bob_box in bob_set:
            return [alice_box, bob_box]
