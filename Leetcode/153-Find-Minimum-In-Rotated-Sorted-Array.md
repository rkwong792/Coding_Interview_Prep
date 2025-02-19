# Find Minimum in Rotated Sorted Array

> - Difficulty: Medium
> - Type: Binary Search
> - [link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Solution - Binary Search
- Time complexity: O(log N)
- Space complexity: O(1)

```python
# Find the minimum element in a sorted and rotated array using Binary Search

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums)-1

        # Tips:
        # Use while l < r for problems where you are shrinking a range by adjusting r = mid.
        # Use while l <= r for regular binary search where r = mid - 1.
        while l < r:
            mid = (l+r) // 2

            if nums[mid] > nums[r]:
                # The pivot happens on the right somewhere.
                l = mid + 1
            else:
                r = mid
        
        return nums[l]

```