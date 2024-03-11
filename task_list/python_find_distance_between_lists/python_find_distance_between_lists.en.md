Given two lists of integers `first_list` and `second_list`, and the integer `target`. **_Return the distance value between the two lists_**.

The distance value is defined as the number of elements `first_list[i]` such that there is not any element `second_list[j]` where `abs(first_list[i] - second_list[j]) <= target`.

**_Examples_**:
```python
Input: first_list = [4, 5, 8], second_list = [10, 9, 1, 8], target = 2
Output: 2
Explanation: 
For first_list[0] = 4 we have: 
|4 - 10| = 6 > d = 2 
|4 - 9 | = 5 > d = 2 
|4 - 1| = 3 > d = 2 
|4 - 8| = 4 > d = 2 
For first_list[1] = 5 we have: 
|5 - 10| = 5 > d = 2 
|5 - 9| = 4 > d = 2 
|5 - 1| = 4 > d = 2 
|5 - 8| = 3 > d = 2
For first_list[2] = 8 we have:
|8 - 10| = 2 <= d = 2
|8 - 9| = 1 <= d = 2
|8 - 1| = 7 > d = 2
|8 - 8| = 0 <= d = 2

Input: first_list = [1, 4, 2, 3], second_list = [-4, -3, 6, 10, 20, 30], target = 3
Output: 2

Input: first_list = [2, 1, 100, 3], second_list = [-5, -2, 10, -3, 7], target = 6
Output: 1
```
---
**_Constraints_**:
- 1 <= `len(first_list), len(second_list)` <= 500`
- 1000 <= `first_list[i], second_list[j]` <= 1000
-  0 <= `target` <= 100