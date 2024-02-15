def transpose(matrix: list[list[int]]) -> list[list[int]]:
    first_row, *_ = matrix
    result_matrix = [[] for _ in range(len(first_row))]

    for _, row in enumerate(matrix):
        for elem_idx, elem in enumerate(row):
            result_matrix[elem_idx].append(elem)
    return result_matrix
