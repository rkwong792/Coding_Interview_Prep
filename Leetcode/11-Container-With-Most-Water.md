# Container With Most Water

> - Difficulty: Medium
> - Type: Two Pointers
> - [link](https://leetcode.com/problems/container-with-most-water/)

## Solution 1 - Bruce Force
- Time complexity: O(n^2)
- Space complexity: O(1)

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res = 0
        # loop through every combination
        for l in range(len(height)-1):
            for r in range(l+1, len(height)):
                # calculate the area l*w
                area = (r-l) * min(height[l], height[r])
                res = max(res, area)
        return res
```

## Solution 2 - Linear Time Solution
- Time complexity: O(n)
- Space complexity: O(1)

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return res
```