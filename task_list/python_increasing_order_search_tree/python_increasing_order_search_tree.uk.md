Дано бінарне дерево пошуку. Вам потрібно
реалізувати функцію `increasing_binary_search_tree`, щоб змінити порядок дерева таким чином, щоб крайня ліва комірка у дереві тепер була коренем дерева, і кожна комірка не мала лівого дочірнього елемента та лише один правий дочірній.

Приклад 1:

![ex1](https://assets.leetcode.com/uploads/2020/11/17/ex1.jpg)
```python
Input: root = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
Output: [1, None, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9]

```
Приклад 2:

![ex2](https://assets.leetcode.com/uploads/2020/11/17/ex2.jpg)
```python
Input: root = [5, 1, 7]
Output: [1, None, 5, None, 7]
```

Обмеження:

- Кількість комірок у даному дереві буде в діапазоні `[1, 100]`.
- `0 <= Node.val <= 1000`