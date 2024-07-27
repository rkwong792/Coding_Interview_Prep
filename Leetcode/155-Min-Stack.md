# Two Sum

> - Difficulty: Medium
> - Type: Stack
> - [link](https://leetcode.com/problems/min-stack/)

## Solution
- Time complexity: O(1) for each function
- Space complexity: O(1)
- Trick is to use two stacks. One stack is telling us the values we've added so far in the order that we've added them. 
- The second stack is telling us what is the minimum value that we have we added so far in each position of the stack.

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
```