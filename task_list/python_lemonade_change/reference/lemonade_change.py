def sell_lemonade(bills: list[int]) -> bool:
    fives = tens = 0

    for bill in bills:
        pattern = bool(fives), bool(tens), fives >= 3
        match bill, *pattern:
            case 5, *_:
                fives += 1
            case 10, True, *_:
                fives -= 1
                tens += 1
            case 20, True, True, *_:
                tens -= 1
                fives -= 1
            case 20, *_, True:
                fives -= 3
            case _:
                return False
    return True
