# Evaluate Reverse Polish Notation

> - Difficulty: Medium
> - Type: Stack
> - [link](https://leetcode.com/problems/evaluate-reverse-polish-notation/)

## Solution
- Time complexity: O(n)
- Space complexity: O(n)

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # LIFO Stack

        # 1) When we see a #, put it on the stack
        # 2) When we see a operator, take the last two numbers and apply that operation
        # 3) Put the result of the operation back on the stack

        stack = []

        for token in tokens:
            if token in "+-*/":
                b, a = stack.pop(), stack.pop()

                if token == "+":
                    stack.append(a + b)
                
                elif token == "-":
                    stack.append(a - b)
                
                elif token == "*":
                    stack.append(a * b)
                
                elif token == "/":
                    stack.append(int(a / b)) 
            else:
                stack.append(int(token))

        return stack[0]
```