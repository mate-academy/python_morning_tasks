def reverse_only_letters(string: str) -> str:
    alphabetical_characters = [character for character in string if character.isalpha()]
    reversed_string_list = list(string)

    for index, character in enumerate(string):
        if character.isalpha():
            reversed_string_list[index] = alphabetical_characters.pop()

    return "".join(reversed_string_list)
