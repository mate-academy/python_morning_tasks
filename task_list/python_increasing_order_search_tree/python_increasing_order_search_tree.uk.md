Дано бінарне дерево пошуку. Вам потрібно
реалізувати функцію `increasing_binary_search_tree`, щоб змінити порядок дерева таким чином, щоб крайня ліва комірка у дереві тепер була коренем дерева, і кожна комірка не мала лівого дочірнього елемента та лише один правий дочірній.

Приклад 1:

![ex1](https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg)
```python
Input: root = [5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9]
Output: [1, null, 2, null, 3, null, 4, null, 5, null, 6, null, 7, null, 8, null, 9]

```
Приклад 2:

![ex2](https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg)
```python
Input: root = [5, 1, 7]
Output: [1, null, 5, null, 7]
```

Constraints:

- The number of nodes in the given tree will be in the range `[1, 100]`.
- `0 <= Node.val <= 1000`