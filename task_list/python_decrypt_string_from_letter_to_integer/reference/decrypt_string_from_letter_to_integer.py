from string import ascii_lowercase


def decrypt_string(string: str) -> str:
    alphabet = ascii_lowercase

    char_tracker = ""
    result = ""

    for char in string:
        temp = char
        if char == "#":
            temp = char_tracker[-2:]
            result = result[:-2]
        next_letter = alphabet[int(temp) - 1]
        result += next_letter
        char_tracker += char

    return result
