Ваш друг набирає своє ім'я на клавіатурі. Іноді під час введення символу `c` клавіша може натискатися декілька разів, і символ буде введено 1 або більше разів.

Реалізуйте функцію `is_long_pressed_name` для перевірки введених символів клавіатури. Поверніть `True`, якщо можливо, що це було ім'я вашого друга, причому деякі символи (можливо, жодного) не натискались повторно.


Приклад: 1:
```python
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
```

Приклад 2:
```python
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
```
