def reverse_only_letters(s: str) -> str:
    alphabetical_characters = [character for character in s if character.isalpha()]
    reversed_string_list = list(s)

    for index, character in enumerate(s):
        if character.isalpha():
            reversed_string_list[index] = alphabetical_characters.pop()

    return "".join(reversed_string_list)
