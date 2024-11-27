# Sum of Rectangle Region In A Given Matrix

> - Type: 2D-Arrays
> - Problem Description: Given a matrix of integers of order M*N and coordinates of a rectangular region in the matrix, write code to find the sum of all the elements in that rectangular region.

## Solution
- Time complexity: O(N^2) - Brute Force
- Space complexity: O(1)

```python
class Solution:
    def sumOfRectangle(matrix, topLeft, botRight):

        # row, column
        # 0,0 and 0,3 -> output: 10
        # 0,0 and 1,3 -> output: 36

        startRow = int(topLeft.split(",")[0])
        startColumn = int(topLeft.split(",")[1])

        endRow = int(botRight.split(",")[0])
        endColumn = int(botRight.split(",")[1])

        sum = 0

        for i in range(startRow, endRow + 1): # rows 
            for j in range(startColumn, endColumn + 1): # columns
                sum += matrix[i][j]
        return sum

        # Call the function
        matrix = [[1,2,3,4],[5,6,7,8],[8,7,6,5],[4,3,2,1]]
        topLeft = "0,0"
        botRight = "1,3"
        sumOfRectangle(matrix, topLeft, botRight)
```