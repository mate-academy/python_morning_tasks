Given a list `num_list` of integers sorted in non-decreasing order, there is exactly one integer in the array that occurs more than `25%` of the time, return that integer.
Дано список цілих чисел `num_list`, відсортований у порядку зростання. В списку є рівно одне ціле число, яке зустрічається більше ніж `25%` разів. Поверни це число.

**_Приклади_**:
```python
Input: num_list = [1, 2, 2, 6, 6, 6, 6, 7, 10]
Output: 6

Input: arr = [1, 1]
Output: 1
```
---
**_Обмеження_**:
- 1 <= `len(num_list)` <= $10^4$
- 0 <= `num_list[i]` <= $10^5$