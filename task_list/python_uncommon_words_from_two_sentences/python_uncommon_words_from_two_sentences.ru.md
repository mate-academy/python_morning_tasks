A **sentence** is a string of single-space separated words where each word consists only of lowercase letters.

A word is **uncommon** if it appears exactly once in one of the sentences, and **does not appear** in the other sentence.

Given two **sentences** `first` and `second`, return _a list of all the **uncommon words**_. You may return the answer in **any order**.

Examples:
```python
Input: first = "this apple is sweet", second = "this apple is sour"
Output: ["sweet", "sour"]

Input: first = "apple apple", second = "banana"
Output: ["banana"]
```

Constraints:
- `1 <= len(first), len(second) <= 200`
- `first` and `second` consist of lowercase English letters and spaces;
- `first` and `second` do not have leading or trailing spaces;
- All the words in `first` and `second` are separated by a single space.