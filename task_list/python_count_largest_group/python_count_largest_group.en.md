You are given an integer `number`.

Each number from `1` to `number` is grouped according to the sum of its digits.

**_Return the quantity of groups that have the largest size_**.

**_Examples_**:
```python
Input: number = 13
Output: 4
Explanation: There are total 9 groups. They are grouped according sum of its digits of numbers from 1 to 13:
[1, 10], [2, 11], [3, 12], [4, 13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Input: number = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
```
---
**_Constraints_**:
- 1 <= `number` <= $10^4$