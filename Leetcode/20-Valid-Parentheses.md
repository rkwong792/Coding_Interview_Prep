# Valid Parentheses

> - Difficulty: Easy
> - Type: Stack
> - [link](https://leetcode.com/problems/valid-parentheses/)

## Solution
- Time complexity: O(n) - Iterate through the input string of size n.
- Space complexity:O(n) - The stack could be up to the size of the input n.

```python
class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        closeToOpen = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False
```