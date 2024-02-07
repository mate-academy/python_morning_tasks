You are given a list of integers `nums` and an integer `range_limit`.

In one operation, you can choose any index `i` where `0 <= i < len(nums)` and change `nums[i]` to `nums[i] + x` where `x` is an integer from the range `[-range_limit, range_limit]`. You can apply this operation **at most once** for each index `i`.

The **score** of `nums` is the difference between the maximum and minimum elements in `nums`.

_Return the minimum **score** of `nums` after applying the mentioned operation at most once for each index in it._

Example:
```python
Input: nums = [1], range_limit = 0
Output: 0
Explanation: The score: max(nums) - min(nums) = 1 - 1 = 0

Input: nums = [0, 10], range_limit = 2
Output: 6
Explanation: Change nums to be [2, 8]. The score: max(nums) - min(nums) = 8 - 2 = 6

Input: nums = [1, 3, 6], range_limit = 3
Output: 0
Explanation: Change nums to be [4, 4, 4]. The score: max(nums) - min(nums) = 4 - 4 = 0
```