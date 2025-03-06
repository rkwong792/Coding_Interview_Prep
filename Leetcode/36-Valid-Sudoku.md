# Valid Sudoku

> - Difficulty: Medium
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/valid-sudoku/)

## Solution
- Time complexity: O(1) - (fixed 81 operations)
- Space complexity: O(1) - (fixed small sets)

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Validate Rows
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != ".":
                    s.add(board[i][j])
            
        # Validate Cols
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != ".":
                    s.add(board[j][i])

        # Validate Sub-boxes
        starts = [(0,0), (0,3), (0,6),
                  (3,0), (3,3), (3,6),
                  (6,0), (6,3), (6,6)]
        
        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != ".":
                        s.add(item)
        
        return True
```