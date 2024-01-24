def is_long_pressed_name(name: str, typed: str) -> bool:
    if len(name) > len(typed):
        return False

    name_index = 0
    for char_index in range(len(typed)):
        if name_index < len(name) and name[name_index] == typed[char_index]:
            name_index += 1
        elif char_index == 0 or typed[char_index] != typed[char_index - 1]:
            return False

    return name_index == len(name)
