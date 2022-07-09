# Two Sum

> - Difficulty: Easy
> - Type: Arrays & Hashing
> - [link](https://https://leetcode.com/problems/two-sum/)

## Solution
- Time complexity: O(n) - Iterate 'nums' array
- Space complexity: O(n) - Hash Map

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val -> index
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
```