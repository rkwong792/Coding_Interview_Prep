# Product of Array Except Self

> - Difficulty: Medium
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/product-of-array-except-self/)

## Solution
- Time complexity: O(n)
- Space complexity: O(1)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
```