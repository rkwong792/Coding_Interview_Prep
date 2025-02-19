# Binary Search

> - Difficulty: Medium
> - Type: Search a 2D Matrix
> - [link](https://leetcode.com/problems/search-a-2d-matrix/)

## Solution 1 - Brute Force
- Time complexity: O(m * n)
- Space complexity: O(1)

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True

        return False

```


## Solution 2 - Binary Search
- Time complexity: O(log n * m) or O(log t)
- Space complexity: O(1)

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        t = m * n
        l, r = 0, t-1

        while l <= r:
            mid = (l+r) // 2
            # Once we have mid index, we can calculate i & j
            i = mid // n   # Convert 1D index to 2D row index
            j = mid % n    # Convert 1D index to 2D row index
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                # If the mid element is greater than the target, search in the left half
                r = mid - 1
            else:
                # If the mid element is smaller than the target, search in the right half
                l = mid + 1
        
        return False
```