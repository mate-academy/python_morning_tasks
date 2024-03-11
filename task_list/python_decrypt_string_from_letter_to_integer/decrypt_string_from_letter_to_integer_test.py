from decrypt_string_from_letter_to_integer import decrypt_string


def assert_message(input_string: str, expected_string: str, output_string: str) -> str:
    return f"Failed. For string={input_string}, valid answer={expected_string}. Your output: {output_string}"


def test_base_cases():
    input_data = "10#11#12"
    expected = "jkab"
    result = decrypt_string(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = "1326#"
    expected = "acz"
    result = decrypt_string(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_longer_input_string():
    input_data = "25112#2624#"
    expected = "bealbfx"
    result = decrypt_string(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = "1982734851925#12345678912#2624#"
    expected = "aihbgcdheaiyabcdefghilbfx"
    result = decrypt_string(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_only_digits():
    input_data = "1987546324532452345"
    expected = "aihgedfcbdecbdebcde"
    result = decrypt_string(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = "12"
    expected = "ab"
    result = decrypt_string(input_data)
    assert result == expected, assert_message(input_data, expected, result)


def test_random_cases():
    input_data = "123#78919#54678"
    expected = "awghisedfgh"
    result = decrypt_string(input_data)
    assert result == expected, assert_message(input_data, expected, result)

    input_data = "#".join([str(num) for num in range(10, 27)])
    expected = "jklmnopqrstuvwxybf"
    result = decrypt_string(input_data)
    assert result == expected, assert_message(input_data, expected, result)
