Given the root of a binary search tree. We have to
implement the `increasing_binary_search_tree` function to rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

Example 1:

![ex1](https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg)
```python
Input: root = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
Output: [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]

```
Example 2:

![ex2](https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg)
```python
Input: root = [5, 1, 7]
Output: [1, None, 5, None, 7]
```

Constraints:

- The number of nodes in the given tree will be in the range `[1, 100]`.
- `0 <= Node.val <= 1000`