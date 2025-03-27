# Intersection of Two Arrays

> - Difficulty: Easy
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/intersection-of-two-arrays/)

## Solution
- Time complexity: O(n + m)
- Space complexity: O(n)

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 = set(nums1)
        res = []

        for num in nums2:
            if num in nums1:
                res.append(num)
                nums1.remove(num)
        
        return res
```