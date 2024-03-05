def reformat_string(input_string: str) -> str:
    letters = [char for char in input_string if char.isalpha()]
    digits = [char for char in input_string if char.isdigit()]

    if abs(len(letters) - len(digits)) > 1:
        return ""

    result_string = ""
    condition_flag = len(letters) > len(digits)

    while letters or digits:
        next_symbol = letters.pop() if condition_flag else digits.pop()
        result_string += next_symbol
        condition_flag = not condition_flag

    return result_string
