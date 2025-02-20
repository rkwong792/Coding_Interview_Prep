# Find Peak Element

> - Difficulty: Medium
> - Type: Binary Search
> - [link](https://leetcode.com/problems/find-peak-element/)

## Solution - Binary Search
- Time complexity: O(log N)
- Space complexity: O(1)

```python

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Initialize two pointers for binary search
        left, right = 0, len(nums) - 1  

        # Continue searching while there is more than one element to consider
        while left < right:
            # Find the middle index
            mid = (left + right) // 2  

            # Compare mid with the next element to decide search direction
            if nums[mid] > nums[mid + 1]:  
                # If nums[mid] is greater than nums[mid + 1], a peak must be on the left side
                # (or mid itself could be a peak), so move right pointer to mid
                right = mid  
            else:
                # If nums[mid] is smaller than nums[mid + 1], a peak must be on the right side
                # So move the left pointer to mid + 1
                left = mid + 1  

        # When left == right, we have found a peak index
        return left  # or return right, since both will be the same

```
