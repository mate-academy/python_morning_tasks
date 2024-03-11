from unique_integers_sum_up_to_zero import sum_zero


def assert_message(input_num: int, expected: list[int], output: list[int]) -> str:
    main_msg = f"Returned list should contain {input_num} elements. Sum of elements should be equal to {0}"
    expected_msg = f"Possible valid list={expected}"
    output_msg = f"Your output: {output} with a sum={sum(output)}"
    return f"Failed. {main_msg}. {expected_msg}. {output_msg}."


def get_conditions(res_list: list[int], num: int):
    return [len(res_list) == num, sum(res_list) == 0, len(set(res_list)) == num]


def test_base_cases():
    input_data = 5
    possible_answer = [-7, -1, 1, 3, 4]
    result = sum_zero(input_data)
    conditions = get_conditions(result, input_data)
    assert all(conditions) is True, assert_message(input_data, possible_answer, result)

    input_data = 1
    possible_answer = [0]
    result = sum_zero(input_data)
    conditions = get_conditions(result, input_data)
    assert all(conditions) is True, assert_message(input_data, possible_answer, result)

    input_data = 3
    possible_answer = [1, 0, 1]
    result = sum_zero(input_data)
    conditions = get_conditions(result, input_data)
    assert all(conditions) is True, assert_message(input_data, possible_answer, result)


def test_positive_numbers():
    input_data = 12
    possible_answer = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5, 6, -6]
    result = sum_zero(input_data)
    conditions = get_conditions(result, input_data)
    assert all(conditions) is True, assert_message(input_data, possible_answer, result)

    input_data = 4
    possible_answer = [1, -1, 2, -2]
    result = sum_zero(input_data)
    conditions = get_conditions(result, input_data)
    assert all(conditions) is True, assert_message(input_data, possible_answer, result)


def test_big_numbers():
    input_data = 1000
    result = sum_zero(input_data)
    conditions = get_conditions(result, input_data)
    assert (
        all(conditions) is True
    ), f"Failed. Should work for large numbers={input_data}"
