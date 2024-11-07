# Move Zeroes

> - Difficulty: Easy
> - Type: Two Pointer
> - [link](https://leetcode.com/problems/move-zeroes/)

## Solution
- Time complexity: O(n)
- Space complexity: O(1)

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Key Concepts:
            Two-pointer technique: One pointer (or index) tracks the next non-zero element, and another pointer is used to traverse the array.
            In-place modification: You must modify the array directly without creating a new one (i.e., no extra space except for a few variables).
        """
        
        l = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l] # Tuple Assignment to swap variables
                l+=1

```