from transpose_matrix import transpose


def assert_message(
    matrix: list[list[int]], expected: list[list[int]], output: list[list[int]]
) -> list[list[int]]:
    return (
        f"Failed: Transpose should be {expected} for matrix {matrix}. Output: {output}"
    )


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
    rows = range(1, 4)
    row_elements = range(1, 10)
    matrix = [
        [row_num * row_elem_num for row_elem_num in row_elements] for row_num in rows
    ]
    expected = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9],
        [4, 8, 12],
        [5, 10, 15],
        [6, 12, 18],
        [7, 14, 21],
        [8, 16, 24],
        [9, 18, 27],
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
    power = 10**9
    matrix = [[power, 2 * power], [3 * power, 4 * power]]
    expected = [[power, 3 * power], [2 * power, 4 * power]]
    result = transpose(matrix)
    assert result == expected, assert_message(matrix, expected, result)
