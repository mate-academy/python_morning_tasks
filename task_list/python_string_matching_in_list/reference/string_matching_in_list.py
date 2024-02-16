def string_matching(words: list[str]) -> list[str]:
    words_list = " ".join(words)
    result_list = [word for word in words if words_list.count(word) >= 2]

    return result_list
