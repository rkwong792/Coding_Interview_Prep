# Find Minimum in Rotated Sorted Array

> - Difficulty: Medium
> - Type: Binary Search
> - [link](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Solution 1 - Linear Search
- Time complexity: O(N)
- Space complexity: O(1)

```python
# Find the minimum element in a sorted and rotated array using Linear Search
# Linear Search is defined as a sequential search algorithm that starts at one end and goes through each element of a list until the desired element is found, otherwise the search continues till the end of the data set. It is the easiest searching algorithm.

class Solution:
    def findMin(self, nums):

        smallestElement = nums[0]
        
        for num in nums:
            if num < smallestElement:
                smallestElement = num
                
        return smallestElement

```

## Solution 2 - Binary Search
- Time complexity: O(log N)
- Space complexity: O(1)

```python
# Find the minimum element in a sorted and rotated array using Binary Search

class Solution:
    def findMin(self, nums):

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res

```