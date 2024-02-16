Given a list of string `words`, return _all strings in `words` that is a **substring** of another word_. You can return the answer in **any order**.
A **substring** is a contiguous sequence of characters within a string

**_Examples_**:
```python
Input: words = ["mass", "as", "hero", "superhero"]
Output: ["as", "hero"]
Explanation: "as" - substring of "mass", "hero" - substring of "superhero".
Also a valid answer: ["hero", "as"]

Input: words = ["leetcode", "et", "code"]
Output: ["et", "code"]
Explanation: "et", "code" are substrings of "leetcode".

Input: words = ["blue", "green", "bu"]
Output: []
Explanation: No substrings of another string.
```
---
**_Constraints_**:
- 1 <= `len(words)` <= 100
- 1 <= `len(words[i])` <= 30
- `words[i]` contains only lowercase English letters.
- All the strings of words are unique.