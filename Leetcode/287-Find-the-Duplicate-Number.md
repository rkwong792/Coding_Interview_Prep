# Find the Duplicate Number

> - Difficulty: Medium
> - Type: Linked List
> - [link](https://leetcode.com/problems/find-the-duplicate-number/)

## Solution
- Time complexity: O(n)
- Space complexity: O(1)

```python
class Solution:
    def findDuplicate(nums):
    # Initialize slow and fast pointers
    slow, fast = nums[0], nums[0]

    # Phase 1: Find intersection point in the cycle (by going 2x & 1x )
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find the where the cycle is (by resetting both to 1x speed)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
```