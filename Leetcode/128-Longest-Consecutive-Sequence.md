# Longest Consecutive Sequence

> - Difficulty: Medium
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/longest-consecutive-sequence/)

## Solution
- Time complexity: O(N)
- Space complexity: O(N)
- Sets are significantly faster than lists if you want to check if an item is contained within it. They can only contain unique items though.

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # We use a HashSet to allow O(1) lookups.
        # Checking if an item is in a list is O(n).
        # Time: O(n + n) => O(n)
        # Space: O(n) - Hash Set
        
        # Ex: [5,4,3,2,1]
        # Outer for loop runs n times
        # Inner while loop will run exactly 5 (n) times
        # for the last index, 1.
        
        # For more details, check Approach 3: HashSet and Intelligent Sequence Building on LeetCode.
        
        numSet = set(nums)
        longest = 0

        for n in numSet:
            # check if it's the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
```
