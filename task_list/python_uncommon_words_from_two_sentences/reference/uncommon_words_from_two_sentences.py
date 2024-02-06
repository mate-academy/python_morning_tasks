from collections import Counter


def uncommon_sentences(first: str, second: str) -> list[str]:
    return [
        word
        for word, appearences in Counter(first.split() + second.split()).items()
        if appearences == 1
    ]
