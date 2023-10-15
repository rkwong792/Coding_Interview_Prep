# Valid Anagram

> - Difficulty: Easy
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/valid-anagram/)

## Solution
- Time complexity: O(s + t) - Iterate through both of the strings.
- Space complexity:O(s + t) - Building hash maps potentially up to the size s + t.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT
```