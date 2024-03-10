from replace_elements_with_greatest import replace_elements


def assert_message(input_list: list, expected: list, output: list) -> str:
    return f"Failed. For input={input_list}, the correct answer is {expected}. Output={output}"


def test_base_cases():
    input_data = [17, 18, 5, 4, 6, 1]
    expected = [18, 6, 6, 6, 1, -1]
    output = replace_elements(input_data)
    assert output == expected, assert_message(input_data, expected, output)

    input_data = [400]
    expected = [-1]
    output = replace_elements(input_data)
    assert output == expected, assert_message(input_data, expected, output)


def test_duplicated_elements():
    input_data = [4, 4, 4]
    expected = [4, 4, -1]
    output = replace_elements(input_data)
    assert output == expected, assert_message(input_data, expected, output)

    input_data = [1, 4, 2, 4, 5, 4, 4, 1]
    expected = [5, 5, 5, 5, 4, 4, 1, -1]
    output = replace_elements(input_data)
    assert output == expected, assert_message(input_data, expected, output)


def test_big_numbers():
    input_data = [29000, 14567, 1908, 99723, 176, 5600]
    expected = [99723, 99723, 99723, 5600, 5600, -1]
    output = replace_elements(input_data)
    assert output == expected, assert_message(input_data, expected, output)

    input_data = [100000, 90000, 80000, 17000, 25]
    expected = [90000, 80000, 17000, 25, -1]
    output = replace_elements(input_data)
    assert output == expected, assert_message(input_data, expected, output)


def test_large_list():
    input_data = [elem for elem in range(200, 10**4 + 1)]
    output = replace_elements(input_data)
    conditions = [
        len(output) == 9801,
        output[-1] == -1,
        output[0] == 10**4,
        len(set(output)) == 2,
    ]

    for condition in conditions:
        assert condition is True, "Failed. Should work correctly for large lists"


test_base_cases()
test_duplicated_elements()
test_big_numbers()
test_large_list()
