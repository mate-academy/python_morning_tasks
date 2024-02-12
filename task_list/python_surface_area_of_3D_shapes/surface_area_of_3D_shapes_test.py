from surface_area_of_3D_shapes import surface_area


def test_single_cell_grid_returns_area():
    grid = [[1]]
    assert (
        surface_area(grid) == 6
    ), "Test for a single cell grid. The surface area should be 6."


def test_multiple_cell_grid_returns_correct_area():
    grid = [[1, 2], [3, 4]]
    assert (
        surface_area(grid) == 34
    ), "Test for a multiple cell grid. The surface area should be 34."


def test_grid_with_zero_height_cells_returns_correct_area():
    grid = [[0, 2], [3, 0]]
    assert (
        surface_area(grid) == 24
    ), "Test for a grid with zero height cells. The surface area should be 19."


def test_grid_with_same_height_cells_returns_correct_area():
    grid = [[2, 2], [2, 2]]
    assert (
        surface_area(grid) == 24
    ), "Test for a grid with same height cells. The surface area should be 24."


def test_grid_with_different_height_cells_returns_correct_area():
    grid = [[1, 2], [3, 4]]
    assert (
        surface_area(grid) == 34
    ), "Test for a grid with different height cells. The surface area should be 34."


def test_min_cell_height():
    grid = [[0, 0], [0, 0]]
    assert (
        surface_area(grid) == 0
    ), "Test for a grid with minimum cell height. The surface area should be 0."


def test_max_cell_height():
    grid = [[50, 50], [50, 50]]
    assert (
        surface_area(grid) == 408
    ), "Test for a grid with maximum cell height. The surface area should be 1000."
    print(surface_area(grid))
