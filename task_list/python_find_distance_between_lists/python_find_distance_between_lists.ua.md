Дано два списки із цілими числами `first_list` та `second_list`, а також ціле число `target`. **_Поверни "відстань" між двома списками_**.

Відстань визначається як кількість елементів з `first_list[i]`, для яких не було жодного елемента з `second_list[j]` які б виконували умову: `abs(first_list[i] - second_list[j]) <= target`.

**_Приклади_**:
```python
Input: first_list = [4, 5, 8], second_list = [10, 9, 1, 8], target = 2
Output: 2
Пояснення: 
Для first_list[0] = 4 маємо: 
|4 - 10| = 6 > target = 2 
|4 - 9 | = 5 > target = 2 
|4 - 1| = 3 > target = 2 
|4 - 8| = 4 > target = 2 
Для first_list[1] = 5 будемо мати: 
|5 - 10| = 5 > target = 2 
|5 - 9| = 4 > target = 2 
|5 - 1| = 4 > target = 2 
|5 - 8| = 3 > target = 2
І для first_list[2] = 8 матимемо:
|8 - 10| = 2 <= target = 2
|8 - 9| = 1 <= target = 2
|8 - 1| = 7 > target = 2
|8 - 8| = 0 <= target = 2

Input: first_list = [1, 4, 2, 3], second_list = [-4, -3, 6, 10, 20, 30], target = 3
Output: 2

Input: first_list = [2, 1, 100, 3], second_list = [-5, -2, 10, -3, 7], target = 6
Output: 1
```
---
**_Обмеження_**:
- 1 <= `len(first_list), len(second_list)` <= 500`
- -1000 <= `first_list[i], second_list[j]` <= 1000
-  0 <= `target` <= 100