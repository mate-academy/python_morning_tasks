from uncommon_words_from_two_sentences import uncommon_sentences


def test_base_case():
    first = "this apple is sweet"
    second = "this apple is sour"
    expected = {"sweet", "sour"}

    result = uncommon_sentences(first, second)

    assert len(result) == len(
        expected
    ), f"Failed: result list should contain {len(expected)} words, not {len(result)}"

    assert all(
        True if word in expected else False for word in result
    ), f"Failed: Result list is not correct. Expected: {expected}, Output: {result}"


def test_duplication_in_one_sentence():
    first = "apple apple"
    second = "banana"
    expected = ["banana"]

    result = uncommon_sentences(first, second)

    assert (
        len(result) == 1
    ), f"Failed: Should contain only one word. Expected: {expected}, Output: {result}"
    assert (
        result[0] == expected[0]
    ), f"Failed: Word can appear only once in order to be present in result list. {result[0]} is not unique"


def test_empty_second_sentence():
    sentence_type = ["unique", "duplicated", "combined"]

    def get_sentence(sentence_variant: str):
        mapper = {
            "unique": [
                "hello my dear friend",
                {"hello", "my", "dear", "friend"},
                "Should contain all unique words from first when second is empty",
            ],
            "duplicated": [
                "pew pew pew",
                [],
                "Should return empty list if no unique words in first when second is empty",
            ],
            "combined": [
                "combo combine rust trust truck combiner truck away await ab combine ba",
                {"combo", "rust", "trust", "combiner", "away", "await", "ab", "ba"},
                "Should contain only unique words and ignore duplicates when second is empty",
            ],
        }
        return mapper.get(sentence_variant)

    for sentence in sentence_type:
        (first, expected, hint), second = get_sentence(sentence), ""
        result = uncommon_sentences(first, second)
        if expected:
            assert len(result) == len(
                expected
            ), f"Failed: Should contain {len(expected)} words. Output: {len(result)}"
            assert all(word in expected for word in result), f"Failed: {hint}"

        else:
            assert result == list(expected) == [], f"Failed: {hint}"


def test_similar_sentences():
    first = "the quick brown foxie jumps over the lazy dog"
    second = "the quick brown dog jumps over the lazy fox"
    expected = {"fox", "foxie"}

    result = uncommon_sentences(first, second)

    assert len(expected) == len(
        result
    ), f"Failed: should contain only {len(expected)} unique words. Output: {len(result)}"
    assert all(
        word in expected for word in result
    ), f"Failed: Result list should be equal to {list(expected)}. Output: {result}"


def test_random_letters():
    first = "abcd def abcd xyz"
    second = "ijk def ijk"
    expected = ["xyz"]

    result = uncommon_sentences(first, second)

    assert (
        result == expected
    ), f"Failed: Should contain unique word for both sentences. Expected: {expected}. Output:  {result}"
