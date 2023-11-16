# Best Time to Buy and Sell Stock

> - Difficulty: Easy
> - Type: Sliding Window
> - [link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

## Solution
- Time complexity: O(n)
- Space complexity: O(1)

```python
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res
```