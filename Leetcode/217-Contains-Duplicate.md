# Contains Duplicate

> - Difficulty: Easy
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/contains-duplicate/)

## Solution
- Time complexity: O(n) - Scan list of inputs
- Space complexity: O(n) - Hash Set

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
```