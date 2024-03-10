Given a list `num_list`, replace every element in that list with the greatest element among the elements to its right, and replace the last element with `-1`.

After doing so, return a list.

**_Examples_**:
```python
Input: num_list = [17, 18, 5, 4, 6, 1]
Output: [18, 6, 6, 6, 1, -1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 would be index 1 (18)
- index 1 --> the greatest element to the right of index 1 would be index 4 (6)
- index 2 --> the greatest element to the right of index 2 would be index 4 (6)
- index 3 --> the greatest element to the right of index 3 would be index 4 (6)
- index 4 --> the greatest element to the right of index 4 would be index 5 (1)
- index 5 --> there are no elements to the right of index 5, so we put -1.

Input: num_list = [400]
Output: [-1]
Explanation: There are no elements to the right of index 0.
```
---
**_Constraints_**:
- 1 <= `len(num_list)` <= $10^4$
- 1 <= `num_list[i]` <= $10^5$