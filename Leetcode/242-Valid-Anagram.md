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
        
        for c in s:
            countS[c] = countS.get(c, 0) + 1
            
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        return countS == countT
```