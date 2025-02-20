# Koko Eating Bananas

> - Difficulty: Medium
> - Type: Binary Search
> - [link](https://leetcode.com/problems/koko-eating-bananas/)

## Solution - Binary Search
- Time complexity: O(log N)
- Space complexity: O(1)

```python
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Initialize binary search range: speed can range from 1 to the maximum number of bananas in piles
        l, r = 1, max(piles)
        
        # Binary search to find the optimal eating speed
        while l < r:
            # Middle speed
            k = (l+r) // 2

            # Compute the total hours needed at that speed
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile / k)

            # If the total hours needed is less than or equal to the allowed hours
            if hours_needed <= h:
                # We may be able to slow down the eating speed and still finish in time,
                # so try a smaller speed.
                r = k
            else:
                # If hours_needed is greater than h, we need to eat faster.
                l = k + 1
        
        # Can return either l or r for the smallest valid speed.
        return l
```
