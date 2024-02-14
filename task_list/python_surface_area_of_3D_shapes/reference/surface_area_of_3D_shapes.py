def surface_area(grid: list[list[int]]) -> int:
    grid_size = len(grid)
    total_area = 0

    for row_index in range(grid_size):
        for col_index in range(grid_size):
            if grid[row_index][col_index]:
                total_area += 2
                for adjacent_row, adjacent_col in (
                    (row_index - 1, col_index),
                    (row_index + 1, col_index),
                    (row_index, col_index - 1),
                    (row_index, col_index + 1),
                ):
                    if 0 <= adjacent_row < grid_size and 0 <= adjacent_col < grid_size:
                        total_area += max(
                            grid[row_index][col_index]
                            - grid[adjacent_row][adjacent_col],
                            0,
                        )
                    else:
                        total_area += grid[row_index][col_index]

    return total_area
