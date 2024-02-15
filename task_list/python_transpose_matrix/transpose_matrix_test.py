from transpose_matrix import transpose


def assert_message(
        matrix: list[list[int]], expected: list[list[int]], output: list[list[int]]
) -> list[list[int]]:
    return f"Failed: Transpose should be {expected} for matrix {matrix}. Output: {output}"


def test_basic_cases():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    result = transpose(matrix)
    assert result == expected, assert_message(matrix, expected, result)

    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    result = transpose(matrix)
    assert result == expected, assert_message(matrix, expected, result)


def test_empty_matrix():
    matrix = []
    expected = []
    result = transpose(matrix)
    assert result == expected, assert_message(matrix, expected, result)


def test_rectangular_matrix():
    matrix = [[1, 2], [3, 4], [5, 6]]
    expected = [[1, 3, 5], [2, 4, 6]]
    result = transpose(matrix)
    assert result == expected, assert_message(matrix, expected, result)


def test_large_matrix():
    matrix = [[i * j for j in range(1, 6)] for i in range(1, 6)]
    expected = [
        [1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], 
        [4, 8, 12, 16, 20], [5, 10, 15, 20, 25]
    ]
    result = transpose(matrix)
    assert result == expected, assert_message(matrix, expected, result)


def test_with_negative_numbers_in_matrix():
    matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
    expected = [[-1, -4, -7], [-2, -5, -8], [-3, -6, -9]]
    result = transpose(matrix)
    assert result == expected, assert_message(matrix, expected, result)

    matrix = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    expected = [[1, -4, 7], [-2, 5, -8], [3, -6, 9]]
    result = transpose(matrix)
    assert result == expected, assert_message(matrix, expected, result)


def test_large_values():
    power = 10 ** 9
    matrix = [[power, 2 * power], [3 * power, 4 * power]]
    expected = [[power, 3 * power], [2 * power, 4 * power]]
    result = transpose(matrix)
    assert result == expected, assert_message(matrix, expected, result)
