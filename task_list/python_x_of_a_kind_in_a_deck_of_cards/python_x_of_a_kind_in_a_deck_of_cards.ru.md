You are given an integer array `deck` where `deck[i]` represents the number written on the $i^{th}$ card.

Partition the cards into one or more groups such that:
- Each group has exactly `x` cards where `x > 1`;
- All the cards in one group have the same integer written on them.

Return `True` if such partition is possible, or `False` otherwise.

Example:
```python
Input: deck = [1, 2, 3, 4, 4, 3, 2, 1]
Output: True
Explanation: Possible partition [1, 1], [2, 2], [3, 3], [4, 4]

Input: deck = [1, 1, 1, 2, 2, 2, 3, 3]
Output: False
Explanation: No possible partition.
```