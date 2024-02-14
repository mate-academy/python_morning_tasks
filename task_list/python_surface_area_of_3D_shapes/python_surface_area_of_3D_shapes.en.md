You are given an `n x n` grid where you have placed some `1 x 1 x 1` cubes. Each value `v = grid[i][j]` represents a tower of `v` cubes placed on top of cell `(i, j)`.

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several irregular 3D shapes.

Implement the `surface_area` function to return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.

Example 1:

![Surface Area Example](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid2.jpg)

```python
Input: grid = [[1, 2], [3, 4]]
Output: 34
```

Example 2:

![Surface Area Example](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid4.jpg)

```python
Input: grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Output: 32
```


Example 3:

![Surface Area Example](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid5.jpg)

```python
Input: grid = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
Output: 46
```