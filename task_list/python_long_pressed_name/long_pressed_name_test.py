from reference.long_pressed_name import is_long_pressed_name


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


def test_long_pressed():
    assert is_long_pressed_name(
        "abc", "aabbcc"
    ), "True: Each character is long-pressed."
    assert is_long_pressed_name(
        "abcd", "abccdd"
    ), "True: Function considers this as valid long-pressed."


def test_end_characters():
    assert is_long_pressed_name(
        "abc", "abcc"
    ), "True: Function allows extra characters at the end."
    assert is_long_pressed_name(
        "abc", "abccccc"
    ), "True: 'c' is long-pressed at the end."


def test_start_characters():
    assert is_long_pressed_name(
        "abc", "aabc"
    ), "True: Function allows extra characters at the start."
    assert is_long_pressed_name(
        "abc", "aaabcc"
    ), "True: 'a' is long-pressed at the start."


def test_middle_characters():
    assert is_long_pressed_name(
        "abc", "abbcc"
    ), "True: Function allows extra characters in the middle."
    assert is_long_pressed_name(
        "abc", "aabbbcc"
    ), "True: Characters in the middle are long-pressed."


def test_random_cases():
    assert is_long_pressed_name(
        "random", "rraaannddooommm"
    ), "True: Characters are long-pressed randomly."
    assert is_long_pressed_name(
        "testing", "tteesstiinngg"
    ), "True: Function considers this as valid long-pressed."
