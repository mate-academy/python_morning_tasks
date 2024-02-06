def uncommon_sentences(first: str, second: str) -> list[str]:
    hashmap = {}
    sentence = f"{first} {second}".split()
    for word in sentence:
        if word in hashmap:
            hashmap[word] += 1
            continue
        hashmap[word] = 1
    return [key for key, value in hashmap.items() if value == 1]
