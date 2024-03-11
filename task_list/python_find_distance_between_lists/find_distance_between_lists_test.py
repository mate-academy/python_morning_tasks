from find_distance_between_lists import find_distance_value


def assert_message(expected: int, output: int, **kwargs) -> str:
    input_data_msg = f"Input data: first_list={kwargs['first']}, second={kwargs['second']}, target={kwargs['target']}"
    main_body = f"Distance is incorrect. Your output={output} != {expected}"
    return f"Failed. {input_data_msg}. {main_body}."


def test_base_cases():
    list1 = [4, 5, 8]
    list2 = [10, 9, 1, 8]
    target = 2

    expected_distance = 2
    result = find_distance_value(list1, list2, target)
    assert result == expected_distance, assert_message(
        expected_distance, result, first=list1, second=list2, target=target
    )

    list1 = [1, 4, 2, 3]
    list2 = [-4, -3, 6, 10, 20, 30]
    target = 3

    expected_distance = 2
    result = find_distance_value(list1, list2, target)
    assert result == expected_distance, assert_message(
        expected_distance, result, first=list1, second=list2, target=target
    )

    list1 = [2, 1, 100, 3]
    list2 = [-5, -2, 10, -3, 7]
    target = 6

    expected_distance = 1
    result = find_distance_value(list1, list2, target)
    assert result == expected_distance, assert_message(
        expected_distance, result, first=list1, second=list2, target=target
    )


def test_equal_length():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    target = 2
    expected_distance = 1
    result = find_distance_value(list1, list2, target)
    assert result == expected_distance, assert_message(
        expected_distance, result, list1, list2, target
    )


def test_negative_numbers():
    list1 = [-3, -2, -1]
    list2 = [-10, -9, -8, -10]
    target = 4
    expected_distance = 3
    result = find_distance_value(list1, list2, target)
    assert result == expected_distance, assert_message(
        expected_distance, result, list1, list2, target
    )


def test_target_zeros():
    list1 = [1, 4, 2, 3]
    list2 = [-4, -3, 6, 10, 20, 30]
    target = 0
    expected_distance = 4
    result = find_distance_value(list1, list2, target)
    assert result == expected_distance, assert_message(
        expected_distance, result, list1, list2, target
    )
