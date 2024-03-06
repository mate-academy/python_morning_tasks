**No-Zero integer** is a positive integer that **does not contain any** `0` in its decimal representation.

Given an integer `num`, return _a list of two integers [a, b] where_:
- `a` and `b` are **No-Zero integers**.
- `a + b = num`

The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

---
**_Examples_**:

**Input**: `num = 2`       
**Output**: `[1, 1]`   
**Explanation**: _Let_ `a = 1`, `b = 1`. _Both_ `a`, `b` _are no-zero integers, additionally_ `a + b = 2 = num`_

**Input**: `num = 11`  
**Output**: `[2, 9]`  
**Explanation**: _Let_ `a = 2`, `b = 9`. _Both ints_ `a`, `b` - _are no-zero integers. In addition_ `a + b = 9 = num`.    
_Note that there are other valid answers that can be accepted_:`[8, 3]`.

---
**_Constraints_**:
- 2 <= `num` <= 104