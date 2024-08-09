# Maximum Subarray

> - Difficulty: Medium
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/maximum-subarray/)

## Solution 1 - Linear (Greedy Solution)
- Time complexity: O(n)
- Space complexity: O(1)

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSub = nums[0]
        
        for i in range(1, len(nums)):
            # kadane's algorithm
            nums[i] = max(nums[i], nums[i] + nums[i-1])
            
            maxSub = max(nums[i], maxSub)
            
        return maxSub
```