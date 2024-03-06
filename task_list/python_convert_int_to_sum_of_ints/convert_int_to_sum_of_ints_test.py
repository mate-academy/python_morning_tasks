from convert_int_to_sum_of_ints import convert_into_sum


def result_checker(number: int, num_list: list[int]) -> bool:
    # DO NOT FORGET TO HIDE TESTS ON THE PLATFORM

    for num in num_list:
        while num > 0:
            if num % 10 == 0:
                return False
            num //= 10

    return True if sum(num_list) == number else False


def assert_message(input_num: int, output: list[int], example: list[int]) -> str:
    msg_body = f"Output={output} may contain integers with '0' in decimal representation or their sum is not equal to input={input_num}"
    msg_example = f"Example of correct answer={example}"

    return f"Failed. For {msg_body}. {msg_example}"


def test_base_cases():
    input_data = 2
    valid_example = [1, 1]
    result = convert_into_sum(input_data)
    checked_result = result_checker(input_data, result)
    assert checked_result is True, assert_message(input_data, result, valid_example)

    input_data = 11
    valid_example = [2, 9]
    result = convert_into_sum(input_data)
    checked_result = result_checker(input_data, result)
    assert checked_result is True, assert_message(input_data, result, valid_example)


def test_bigger_input_numbers():
    input_data = 99
    valid_example = [91, 8]
    result = convert_into_sum(input_data)
    checked_result = result_checker(input_data, result)
    assert checked_result is True, assert_message(input_data, result, valid_example)

    input_data = 85
    valid_example = [84, 1]
    result = convert_into_sum(input_data)
    checked_result = result_checker(input_data, result)
    assert checked_result is True, assert_message(input_data, result, valid_example)


def test_input_number_with_zeros():
    input_data = 100
    valid_example = [1, 99]
    result = convert_into_sum(input_data)
    checked_result = result_checker(input_data, result)
    assert checked_result is True, assert_message(input_data, result, valid_example)

    input_data = 104
    valid_example = [99, 5]
    result = convert_into_sum(input_data)
    checked_result = result_checker(input_data, result)
    assert checked_result is True, assert_message(input_data, result, valid_example)
