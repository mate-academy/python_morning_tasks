from long_pressed_name import Solution


def test_basic_true_cases():
    solution = Solution()
    assert solution.isLongPressedName("alex", "aaleex")
    assert solution.isLongPressedName("leelee", "lleeelee")
    assert solution.isLongPressedName("laiden", "laiden")
    assert solution.isLongPressedName("sam", "ssaaammm")
    assert solution.isLongPressedName("john", "jjjooohhhnnn")
    assert solution.isLongPressedName("anna", "aaaaannnnnaaaa")


def test_basic_false_cases():
    solution = Solution()
    assert not solution.isLongPressedName("saeed", "ssaaedd")
    assert not solution.isLongPressedName("julia", "juuliaa")
    assert not solution.isLongPressedName("alex", "aaleeex")
    assert not solution.isLongPressedName("natasha", "nattasha")


def test_empty_strings():
    solution = Solution()
    assert not solution.isLongPressedName("", "a")
    assert solution.isLongPressedName("", "")


def test_single_character():
    solution = Solution()
    assert solution.isLongPressedName("a", "a")
    assert solution.isLongPressedName("b", "bbbb")


def test_mismatched_characters():
    solution = Solution()
    assert not solution.isLongPressedName("ab", "ac")
    assert not solution.isLongPressedName("cd", "dc")


def test_long_pressed():
    solution = Solution()
    assert solution.isLongPressedName("abc", "aabbcc")
    assert not solution.isLongPressedName("abcd", "abccdd")


def test_end_characters():
    solution = Solution()
    assert not solution.isLongPressedName("abc", "abcc")
    assert solution.isLongPressedName("abc", "abccccc")


def test_start_characters():
    solution = Solution()
    assert not solution.isLongPressedName("abc", "aabc")
    assert solution.isLongPressedName("abc", "aaabcc")


def test_middle_characters():
    solution = Solution()
    assert not solution.isLongPressedName("abc", "abbcc")
    assert solution.isLongPressedName("abc", "aabbbcc")


def test_random_cases():
    solution = Solution()
    assert solution.isLongPressedName("random", "rraaannddooommm")
    assert not solution.isLongPressedName("testing", "tteesstiinngg")
    assert not solution.isLongPressedName("python", "pyythhoonn")
    assert solution.isLongPressedName("code", "coooodeee")


def test_typed_shorter_than_name():
    solution = Solution()
    assert not solution.isLongPressedName("abcd", "abc")
    assert not solution.isLongPressedName("hello", "hell")


def test_case_sensitivity():
    solution = Solution()
    assert not solution.isLongPressedName("Case", "case")
    assert solution.isLongPressedName("Case", "Caaase")
