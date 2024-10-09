# Longest Substring Without Repeating Characters

> - Difficulty: Medium
> - Type: Sliding Window
> - [link](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

- Time complexity: O(n) - Even though we have two loops, in the inner while loop will run at most 'n' times, not per iteration of 'r'
- Space complexity: O(n) - Set
- Greg Hogg for explaination - https://www.youtube.com/watch?v=FCbOzdHKW18

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
```
