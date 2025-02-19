# Search in Rotated Sorted Array 

> - Difficulty: Medium
> - Type: Binary Search
> - [link](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Solution - Binary Search
- Time complexity: O(log N)
- Space complexity: O(1)

```python

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # Step 1: Find the index of the smallest element (pivot)
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:  
                l = m + 1  # Pivot is on the right half
            else:
                r = m  # Pivot is on the left half (or at mid)

        min_i = l  # Pivot index (smallest element's index)

        # Step 2: Determine which sorted half to perform binary search on
        if min_i == 0:
            l, r = 0, len(nums) - 1
        elif target >= nums[0] and target <= nums[min_i - 1]:  
            l, r = 0, min_i - 1  # Search in left sorted half
        else:
            l, r = min_i, len(nums) - 1  # Search in right sorted half

        # Step 3: Standard binary search
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m  # Target found
            elif nums[m] < target:
                l = m + 1  # Search right half
            else:
                r = m - 1  # Search left half

        return -1  # Target not found
```