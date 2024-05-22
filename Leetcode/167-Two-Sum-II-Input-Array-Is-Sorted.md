# Two Sum II - Input Array Is Sorted

> - Difficulty: Medium
> - Type: Two Pointers
> - [link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Solution
- Time complexity: O(n) - Need to iterate through the entire list of size n.
- Space complexity: O(1) - Constant space. This algorithm allocates the same amount of memory irrespective of the size of the list.

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
```