Дано список цілих чисел `nums`, половина цілих чисел у `nums` є непарними, а інша половина - парними.

Реалізуйте функцію `sort_list_by_parity`, щоб відсортувати список таким чином, що якщо `nums[i]` є непарним, `i` буде непарним, а якщо `nums[i]` парним, `i` буде парним.

Повертає будь-який список відповідей, який задовольняє цю умову.


Приклад:
```python
Input: nums = [4, 2, 5, 7]
Output: [4, 5, 2, 7]
Explanation: [4, 7, 2, 5], [2, 5, 4, 7], [2, 7, 4, 5] would also have been accepted.

Input: nums = [2, 3]
Output: [2, 3]

```

