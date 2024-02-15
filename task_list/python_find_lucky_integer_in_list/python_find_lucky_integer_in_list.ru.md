Given a list of integers `nums`, a **lucky integer** is an integer that has a frequency in the list equal to its value.

Return _the largest **lucky integer** in the list_. If there is no **lucky integer** return `-1`.

**_Examples_**:
```python
Input: nums = [2, 2, 3, 4]
Output: 2
Explanation: The only lucky number here would be 2. Because frequency[2] == 2.


Input: nums = [1, 2, 2, 3, 3, 3]
Output: 3
Explanation: 1, 2, 3 are lucky numbers, result should be the largest of them.

Input: nums = [2, 2, 2, 3, 3]
Output: -1
Explanation: There are no lucky numbers.
```
---
**_Constraints_**:
- 1 <= `len(arr)` <= 500
- 1 <= `arr[i]` <= 500