# Sort Colors

> - Difficulty: Medium
> - Type: Two Pointers
> - [link](https://leetcode.com/problems/sort-colors/)
> - "Dutch Flag Algorithm"
## Solution
- Time complexity: O(n)
- Space complexity: O(1) (in-place)

```python
class Solution:
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Key Concepts:
            Two-pointer technique
            In-place sorting - We don't use extra space
            Partitioning problem - Dividng the array into multiple sections
        """

        l, r = 0, len(nums)-1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                i+=1
                l+=1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r-=1
            else:
                i+=1
```