# Valid Palindrome

> - Difficulty: Easy
> - Type: Two Pointers
> - [link](https://leetcode.com/problems/valid-palindrome/)

## Solution
- Time complexity: O(n) - Need to iterate through the the entire string of size n.
- Space complexity: O(n) - Allocate space to build our new string of size n.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newString = ""

        # Build a new string
        for c in s:
            if c.isalnum():
                newString += c.lower()
        
        # Two pointers
        l = 0
        r = len(newString)-1

        while l < r:
            if newString[l] != newString[r]:
                return False
            l+=1
            r-=1
        
        return True
```