# Find First and Last Position of Element in Sorted Array

> - Difficulty: Medium
> - Type: Binary Search
> - [link](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Solution - Binary Search
- Time complexity: O(log N)
- Space complexity: O(1)
- *Hint: When we find target, we continue searching left for the first occurrence and right for the last occurrence.*

```python
class Solution:
  def searchRange(nums, target):
      def findFirst(nums, target):
          left, right = 0, len(nums) - 1
          first = -1
          while left <= right:
              mid = (left + right) // 2
              if nums[mid] >= target:
                  right = mid - 1
              else:
                  left = mid + 1
              if nums[mid] == target:
                  first = mid
          return first
      
      def findLast(nums, target):
          left, right = 0, len(nums) - 1
          last = -1
          while left <= right:
              mid = (left + right) // 2
              if nums[mid] <= target:
                  left = mid + 1
              else:
                  right = mid - 1
              if nums[mid] == target:
                  last = mid
          return last
  
      return [findFirst(nums, target), findLast(nums, target)]
```
