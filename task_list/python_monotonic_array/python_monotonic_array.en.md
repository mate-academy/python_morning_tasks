A list is **monotonic** if it is either monotone increasing or monotone decreasing.
A `nums` list is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. A `nums` list is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given a list of integers `nums`, return `True` _if the given list is monotonic, or `False` otherwise_.

**_Examples_**:
```python
Input: nums = [1, 2, 2, 3]
Output: True

Input: nums = [6, 5, 4, 4]
Output: True

Input: nums = [1, 3, 2]
Output: False
```
---
**_Constraints_**:
- 1 <= `len(nums)` <= 105
- -105 <= `nums[i]` <= 105