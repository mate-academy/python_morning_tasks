At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20` bill. You must provide the correct change to each customer so that the net transaction is that the customer pays `$5`.

Note that you do not have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the $i^{th}$ customer pays, return `True` if you can provide **every customer** with the correct change, or `False` otherwise.

### Example 1:
```python
    Input: bills = [5, 5, 5, 10, 20]
    Output: True
```
**_Explanation_**:
<em>
- Three customers at the beginning give us three `$5` bills;
- From the fourth customer, we collect a `$10` bill, give back a `$5`;
- From the fifth customer, we get a `$10` bill, giving `$5` bill back;
- Since every customer got correct change, we output `True`.
</em>

### Example 2:
```python
Input: bills = [5, 5, 10, 10, 20]
Output: False
```
**_Explanation_**:
<em>
- From the first two customers, we collect two `$5` bills;
- From the following two customers, we collect a `$10` bill, giving back a `$5` bill;
- For the last customer, we can not give the change of `$15` back because we only have two `$10` bills;
- Since not every customer received the correct change, the answer we should return `False`.
</em>

**_Constraints_**:
- 1 <= `len(bills)` <= 105
- `bills[i]` is either `5$`, `10$`, or `20$`