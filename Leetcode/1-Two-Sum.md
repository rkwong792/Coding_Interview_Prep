# Two Sum

> - Difficulty: Easy
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/two-sum/)

## Solution 1 - Brute Force
- Time complexity: O(n^2)
- Space complexity: O(1)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i, j]
```


## Solution 2 - One Pass Hash Map
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