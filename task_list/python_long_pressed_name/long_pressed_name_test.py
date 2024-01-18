from long_pressed_name import is_long_pressed_name


def test_basic_true_cases():
    """Test basic cases where the typed name is a valid long-pressed version of the name."""
    assert is_long_pressed_name("alex", "aaleex")
    assert is_long_pressed_name("leelee", "lleeelee")
    assert is_long_pressed_name("laiden", "laiden")
    assert is_long_pressed_name("sam", "ssaaammm")
    assert is_long_pressed_name("john", "jjjooohhhnnn")
    assert is_long_pressed_name("anna", "aaaaannnnnaaaa")


def test_basic_false_cases():
    """Test basic cases where the typed name is not a valid long-pressed version of the name."""
    assert not is_long_pressed_name("saeed", "ssaaedd")
    assert not is_long_pressed_name("julia", "juuliaa")
    assert not is_long_pressed_name("alex", "aaleeex")
    assert not is_long_pressed_name("natasha", "nattasha")


def test_empty_strings():
    """Test cases with empty strings."""
    assert not is_long_pressed_name("", "a")
    assert is_long_pressed_name("", "")


def test_single_character():
    """Test cases with single character names."""
    assert is_long_pressed_name("a", "a")
    assert is_long_pressed_name("b", "bbbb")


def test_mismatched_characters():
    """Test cases where characters do not match."""
    assert not is_long_pressed_name("ab", "ac")
    assert not is_long_pressed_name("cd", "dc")


def test_long_pressed():
    """Test longer cases of long-pressed names."""
    assert is_long_pressed_name("abc", "aabbcc")
    assert not is_long_pressed_name("abcd", "abccdd")


def test_end_characters():
    """Test cases where extra characters are added at the end."""
    assert not is_long_pressed_name("abc", "abcc")
    assert is_long_pressed_name("abc", "abccccc")


def test_start_characters():
    """Test cases where extra characters are added at the start."""
    assert not is_long_pressed_name("abc", "aabc")
    assert is_long_pressed_name("abc", "aaabcc")


def test_middle_characters():
    """Test cases where extra characters are added in the middle."""
    assert not is_long_pressed_name("abc", "abbcc")
    assert is_long_pressed_name("abc", "aabbbcc")


def test_random_cases():
    """Test various random cases."""
    assert is_long_pressed_name("random", "rraaannddooommm")
    assert not is_long_pressed_name("testing", "tteesstiinngg")
    assert not is_long_pressed_name("python", "pyythhoonn")
    assert is_long_pressed_name("code", "coooodeee")


def test_typed_shorter_than_name():
    """Test cases where the typed name is shorter than the actual name."""
    assert not is_long_pressed_name("abcd", "abc")
    assert not is_long_pressed_name("hello", "hell")


def test_case_sensitivity():
    """Test cases to check for case sensitivity."""
    assert not is_long_pressed_name("Case", "case")
    assert is_long_pressed_name("Case", "Caaase")
