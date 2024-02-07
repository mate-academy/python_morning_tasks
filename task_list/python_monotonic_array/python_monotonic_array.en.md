An array is **monotonic** if it is either monotone increasing or monotone decreasing.
An array `nums` is monotone increasing if for all `i <= j`, `nums[i] <= nums[j]`. An array nums is monotone decreasing if for all `i <= j`, `nums[i] >= nums[j]`.

Given an integer array `nums`, return `True` _if the given array is monotonic, or `False` otherwise_.

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