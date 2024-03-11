На вхід дається список цілих чисел `nums`. Ти починаєш з початкового **позитивного** значення, назвемо його _start_value_.

На кожній ітерації ти покроково обчислюєш суму _start_value_ плюс елементи в `nums` (зліва направо).

Поверни **мінімальне додатне** значення _start_value_ таким чином, щоб покрокова сума ніколи не була меншою за `1`.

**_Приклади_**:
```python
Input: nums = [-3, 2, -3, 4, 2]
Output: 5
Пояснення: якщо ти візьмеш start_value = 4, у третій ітерації твоя покрокова сума буде меншою за 1.
Розрахунок "покрокової суми":
- start_value = 4
    (4 - 3) = 1
    (1 + 2) = 3
    (3 - 3) = 0 -> саме тут покрокова сума стала меншою за 1
    (0 + 4) = 4
    (4 + 2) = 6
- start_value = 5
    (5 - 3) = 2
    (2 + 2) = 4
    (4 - 3) = 1
    (1 + 4) = 5
    (5 + 2) = 7

Input: nums = [1, 2]
Output: 1
Пояснення: Мінімальне початкове значення має бути додатним.

Input: nums = [1, -2, -3]
Output: 5
```
---
**_Обмеження_**:
- 1 <= `len(nums)` <= 100
- -100 <= `nums[i]` <= 100