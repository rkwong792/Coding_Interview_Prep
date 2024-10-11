# Longest Consecutive Sequence

> - Difficulty: Medium
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/longest-consecutive-sequence/)

## Solution
- Time complexity: O(N)
- Space complexity: O(N)
- Sets are significantly faster than lists if you want to check if an item is contained within it. They can only contain unique items though.
- https://www.youtube.com/watch?v=joIEdeOGqjQ

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # We use a HashSet to allow O(1) lookups.
        # Time: O(n)
        # Space: O(n) - Hash Set
                
        # For more details, check Approach 3: HashSet and Intelligent Sequence Building on LeetCode.
        
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num-1) not in numSet:
                next_num = num + 1                
                length = 1
                while next_num in numSet:
                    next_num +=1
                    length +=1
                longest = max(longest, length)
        
        return longest
```
