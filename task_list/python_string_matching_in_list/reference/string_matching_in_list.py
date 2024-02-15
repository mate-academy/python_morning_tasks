def string_matching(words: list[str]) -> list[str]:
    def is_substring(first, second):
        return first in second

    words.sort(key=len)
    result = []
    for first_idx in range(len(words)):
        for second_idx in range(first_idx + 1, len(words)):
            if is_substring(words[first_idx], words[second_idx]):
                result.append(words[first_idx])
                break
    return result
