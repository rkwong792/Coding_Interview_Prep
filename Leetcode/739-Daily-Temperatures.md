# Daily Temperatures

> - Difficulty: Medium
> - Type: Stack
> - [link](https://leetcode.com/problems/daily-temperatures/)

## Solution
- Time complexity: O(n)
- Space complexity: O(n)
- *Monotonic decreasing stack - You use a stack to keep track of indices of temperatures in a monotonic decreasing order.*
- *As you iterate through the list, you pop elements from the stack when you find a temperature that is warmer than the temperature at the index stored at the top of the stack.*

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                stack_i, stack_t = stack.pop()
                res[stack_i] = i - stack_i
            
            stack.append((i, t))
        
        return res

```