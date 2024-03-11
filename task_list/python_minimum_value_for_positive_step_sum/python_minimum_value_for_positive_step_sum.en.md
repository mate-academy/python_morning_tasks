Given a list of integers `nums`, you start with an initial **positive** value _start_value_.

In each iteration, you calculate the step by step sum of _start_value_ plus elements in `nums` (from left to right).

Return the **minimum positive** value of _start_value_ such that the step by step sum is never less than `1`.

**_Examples_**:
```python
Input: nums = [-3, 2, -3, 4, 2]
Output: 5
Explanation: If you choose start_value = 4, in the third iteration your step by step sum is less than 1.
step by step sum:
- start_value = 4
    (4 - 3) = 1
    (1 + 2) = 3
    (3 - 3) = 0 -> step sum is less than 1
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
Explanation: Minimum start value should be positive. 

Input: nums = [1, -2, -3]
Output: 5
```
---
**_Constraints_**:
- 1 <= `len(nums)` <= 100
- 100 <= `nums[i]` <= 100