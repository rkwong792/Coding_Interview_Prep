# Binary Search

> - Difficulty: Easy
> - Type: Binary Search
> - [link](https://leetcode.com/problems/binary-search/)

## Solution
- Time complexity: O(Log n)
- Space complexity: O(1)

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2 # Divison operation rounds down

            if nums[mid] > target:
                # we want to search left side
                r = mid - 1
            elif nums[mid] < target:
                # we want to search right side
                l = mid + 1
            else:
                return mid
        return -1
```