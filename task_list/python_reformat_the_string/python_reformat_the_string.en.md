You are given an alphanumeric string `input_string`. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return _the reformatted string_ or return **an empty string** if it is impossible to reformat the string.


**_Examples_**:
```python
Input: input_string = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters are digits nor letters "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

Input: input_string = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.

Input: input_string = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.
```
---
**_Constraints_**:
- 1 <= `len(input_string)` <= 500
- `input_string` consists of only lowercase English letters and/or digits.