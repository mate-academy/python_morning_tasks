from long_pressed_name import is_long_pressed_name


def test_basic_true_cases():
    assert is_long_pressed_name("alex", "aaleex"), "True: 'a' and 'e' are long-pressed."
    assert is_long_pressed_name(
        "leelee", "lleeelee"
    ), "True: 'l' and 'e' are long-pressed."
    assert is_long_pressed_name("laiden", "laiden"), "True: Typed exactly as the name."
    assert is_long_pressed_name(
        "sam", "ssaaammm"
    ), "True: All characters are long-pressed."
    assert is_long_pressed_name(
        "john", "jjjooohhhnnn"
    ), "True: All characters are long-pressed."
    assert is_long_pressed_name(
        "anna", "aaaaannnnnaaaa"
    ), "True: All characters are long-pressed."


def test_basic_false_cases():
    assert not is_long_pressed_name(
        "saeed", "ssaaedd"
    ), "False: 'e' and 'd' do not match."
    assert not is_long_pressed_name(
        "julia", "juuliaa"
    ), "False: 'u' and 'a' are incorrectly long-pressed."
    assert not is_long_pressed_name(
        "alex", "aaleeex"
    ), "False: 'e' is long-pressed incorrectly."
    assert not is_long_pressed_name(
        "natasha", "nattasha"
    ), "False: 't' is long-pressed incorrectly."


def test_empty_strings():
    assert not is_long_pressed_name(
        "", "a"
    ), "False: Non-empty typed string from empty name."
    assert is_long_pressed_name("", ""), "True: Both strings are empty."


def test_single_character():
    assert is_long_pressed_name("a", "a"), "True: Single character matches."
    assert is_long_pressed_name(
        "b", "bbbb"
    ), "True: Single character 'b' is long-pressed."


def test_mismatched_characters():
    assert not is_long_pressed_name(
        "ab", "ac"
    ), "False: Characters 'b' and 'c' do not match."
    assert not is_long_pressed_name(
        "cd", "dc"
    ), "False: Characters 'c' and 'd' are in the wrong order."


def test_long_pressed():
    assert is_long_pressed_name(
        "abc", "aabbcc"
    ), "True: Each character is long-pressed."
    assert not is_long_pressed_name(
        "abcd", "abccdd"
    ), "False: 'b' and 'c' are pressed incorrectly."


def test_end_characters():
    assert not is_long_pressed_name(
        "abc", "abcc"
    ), "False: Extra character 'c' at the end."
    assert is_long_pressed_name(
        "abc", "abccccc"
    ), "True: 'c' is long-pressed at the end."


def test_start_characters():
    assert not is_long_pressed_name(
        "abc", "aabc"
    ), "False: Extra character 'a' at the start."
    assert is_long_pressed_name(
        "abc", "aaabcc"
    ), "True: 'a' is long-pressed at the start."


def test_middle_characters():
    assert not is_long_pressed_name(
        "abc", "abbcc"
    ), "False: Extra characters in the middle."
    assert is_long_pressed_name(
        "abc", "aabbbcc"
    ), "True: Characters in the middle are long-pressed."


def test_random_cases():
    assert is_long_pressed_name(
        "random", "rraaannddooommm"
    ), "True: Characters are long-pressed randomly."
    assert not is_long_pressed_name(
        "testing", "tteesstiinngg"
    ), "False: Characters are pressed incorrectly."
    assert not is_long_pressed_name(
        "python", "pyythhoonn"
    ), "False: Characters are pressed incorrectly."
    assert is_long_pressed_name(
        "code", "coooodeee"
    ), "True: Characters 'o' and 'e' are long-pressed."


def test_typed_shorter_than_name():
    assert not is_long_pressed_name(
        "abcd", "abc"
    ), "False: Typed string is shorter than the name."
    assert not is_long_pressed_name(
        "hello", "hell"
    ), "False: Typed string is missing characters."


def test_case_sensitivity():
    assert not is_long_pressed_name("Case", "case"), "False: Case sensitivity mismatch."
    assert is_long_pressed_name(
        "Case", "Caaase"
    ), "True: 'a' is long-pressed, case matches."
