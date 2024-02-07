def sell_lemonade(bills: list[int]) -> bool:
    fives = tens = 0

    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10 and fives:
            tens += 1
            fives -= 1
        elif bill == 20 and fives and tens:
            tens -= 1
            fives -= 1
        elif bill == 20 and fives >= 3:
            fives -= 3
        else:
            return False
    return True
