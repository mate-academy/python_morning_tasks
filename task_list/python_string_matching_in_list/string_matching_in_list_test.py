from string_matching_in_list import string_matching


def assert_message(words: list[str], expected: list[str], output: list[str]) -> str:
    return f"Failed: Should return {expected} in any order for words={words}. Output: {output}"


def test_base_cases():
    words = ["mass", "as", "hero", "superhero"]
    expected = ["as", "hero"]
    result = string_matching(words)
    assert sorted(result, key=len) == expected, assert_message(words, expected, result)

    words = ["leetcode", "et", "code"]
    expected = ["et", "code"]
    result = string_matching(words)
    assert sorted(result, key=len) == expected, assert_message(words, expected, result)

    words = ["blue", "green", "bu"]
    expected = []
    result = string_matching(words)
    assert result == expected, assert_message(words, expected, result)


def test_single_element_list():
    words = ["lol"]
    expected = []
    result = string_matching(words)
    assert result == expected, assert_message(words, expected, result)


def test_all_words_substrings():
    words = ["a", "ab", "abc", "abcd"]
    expected = ["a", "ab", "abc"]
    result = string_matching(words)
    assert sorted(result, key=len) == expected, assert_message(words, expected, result)


def test_random_substrings_and_non_substrings():
    words = ["cat", "car", "card", "art", "artificial"]
    expected = ["art", "car"]
    result = string_matching(words)
    assert sorted(result) == expected, assert_message(words, expected, result)


def test_long_words():
    words = [
        "programming",
        "multithreading",
        "program",
        "supernovae",
        "hollyroller",
        "threading",
        "holly",
        "roller",
        "novae",
    ]
    expected = ["holly", "novae", "roller", "program", "threading"]
    result = string_matching(words)
    assert sorted(result, key=len) == expected, assert_message(words, expected, result)


def test_almost_substrings():
    words = ["abc", "abs", "bfgh", "bfhg", "grey", "gray"]
    expected = []
    result = string_matching(words)
    assert result == expected, assert_message(words, expected, result)


def test_substrings_beginning_or_end():
    words = ["abc", "bc", "a"]
    expected = ["a", "bc"]
    result = string_matching(words)
    assert sorted(result, key=len) == expected, assert_message(words, expected, result)

    words = ["um", "ami", "umami", "ma"]
    expected = ["um", "ma", "ami"]
    result = string_matching(words)
    assert sorted(result, key=len) == expected, assert_message(words, expected, result)


def test_large_number_of_strings():
    import string

    initial = "initial"
    words = [initial + string.ascii_lowercase[:index] for index in range(26)]
    expected = words[:-1]
    result = string_matching(words)
    assert sorted(result, key=len) == expected, assert_message(words, expected, result)
