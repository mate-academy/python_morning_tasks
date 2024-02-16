Alice and Bob have a different total number of candies. You are given two lists with integers inside: `alice_candies` and `bob_candies` where `alice_candies[i]` is the number of candies of the $i^{th}$ box of candy that Alice has and `bob_candies[j]` is the number of candies of the $j^{th}$ box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

Return _an `answer` - a list of integers where `answer[0]` is the number of candies in the box that Alice must exchange, and `answer[1]` is the number of candies in the box that Bob must exchange. If there are multiple answers, you may **return any** one of them. It is guaranteed that at least one answer exists_.

**_Examples_**:
```python
Input: alice_candies = [1, 1], bob_candies = [2, 2]
Output: [1, 2]

Input: alice_candies = [1, 2], bob_candies = [2, 3]
Output: [1, 2]

Input: alice_candies = [2], bob_candies = [1, 3]
Output: [2, 3]
```
---
**_Constraints_**:
- 1 <= `len(alice_candies), len(bob_candies)` <= $10^4$
- 1 <= `alice_candies[i]`, `bob_candies[j]` <= $10^5$
- Alice and Bob have a different total number of candies.
- There will be at least one valid answer for the given input.