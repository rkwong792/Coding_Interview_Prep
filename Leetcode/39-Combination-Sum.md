# Combination Sum

> - Difficulty: Medium
> - Type: Backtracking
> - [link](https://leetcode.com/problems/combination-sum)

## Solution
Leetcode/images/Time & Space Complexity - LC 39.png

```python
class Solution:
    def combinationSum(candidates, target):
        result = []  # This list will hold all the valid combinations.

        def backtrack(start, path, total):
            # If we've reached the target sum, record the current combination.
            if total == target:
                result.append(path[:])  # Append a copy of the current combination.
                return
            
            # If the total exceeds the target, no need to continue exploring this path.
            if total > target:
                return
            
            # Try each candidate starting from the current index.
            # Using 'start' ensures we can reuse the same number.
            for i in range(start, len(candidates)):
                # Choose the candidate.
                path.append(candidates[i])
                # Recursively explore further with the chosen candidate.
                backtrack(i, path, total + candidates[i])
                # Backtrack: undo the last choice to try the next candidate.
                path.pop()
        
        # Start backtracking from index 0, with an empty path and sum = 0.
        backtrack(0, [], 0)
        return result
```