Given an list of integers `nums`, half of the integers in `nums` are odd, and the other half are even.

Implement the `sort_list_by_parity` function to sort the list so that whenever `nums[i]` is odd, `i` is odd, and whenever `nums[i]` is even, `i` is even.

Return any answer list that satisfies this condition.

Example:
```python
Input: nums = [4, 2, 5, 7]
Output: [4, 5, 2, 7]
Explanation: [4, 7, 2, 5], [2, 5, 4, 7], [2, 7, 4, 5] would also have been accepted.

Input: nums = [2, 3]
Output: [2, 3]
```