Вам надається сітка `n x n`, де ви розмістили кілька кубиків `1 x 1 x 1`. Кожне значення `v = grid[i][j]` представляє вежу з `v` кубів, розташованих на вершині клітинки `(i, j)`.

Розмістивши ці куби, ви вирішили об'єднати будь-які безпосередньо сусідні куби один з одним, утворюючи кілька неправильних тривимірних форм.

Реалізуйте функцію `surface_area`, щоб повернути загальну площу поверхні отриманих форм.

Примітка. Нижня грань кожної фігури враховується до її площі.



Приклад 1:

![Surface Area Example](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid2.jpg)

```python
Input: grid = [[1, 2], [3, 4]]
Output: 34
```

Приклад 2:

![Surface Area Example](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid4.jpg)

```python
Input: grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
Output: 32
```


Приклад 3:

![Surface Area Example](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid5.jpg)

```python
Input: grid = [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
Output: 46
```