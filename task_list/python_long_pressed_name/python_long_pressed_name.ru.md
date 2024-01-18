Your friend is typing his `name` into a keyboard. Sometimes, when typing a character `c`, the key might get long pressed, and the character will be typed 1 or more times.

Implement the `is_long_pressed_name` function to examine the typed characters of the keyboard. Return `True` if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:
```python
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
```

Example 2:
```python
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
```
