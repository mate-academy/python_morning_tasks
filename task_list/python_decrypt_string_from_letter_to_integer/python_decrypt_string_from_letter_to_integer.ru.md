You are given a string `string` formed by digits and `#`. We want to map `string` to English lowercase characters as follows:
- Characters (`a` to `i`) are represented by (`1` to `9`) respectively
- Characters (`j` to `z`) are represented by (`10#` to `26#`) respectively

Return _the string formed after mapping_.

The test cases are generated so that a unique mapping will always exist.

**_Examples_**:
```python
Input: string = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2"

Input: string = "1326#"
Output: "acz"
```
---
**_Constraints_**:
- 1 <= `len(string)` <= 1000
- `string` consists of digits and the `#` letter
- `string` will be a valid string such that mapping is always possible