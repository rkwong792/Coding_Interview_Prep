# Key Sequencer

> - Type: Arrays
> - Problem Description: Given a matrix of integers of order M*N and coordinates of a rectangular region in the matrix, write code to find the sum of all the elements in that rectangular region.

> - Imagine you have a special keyboard with the following keys: Key 1:  Prints 'A' on screen, Key 2: (Ctrl-A): Select screen, Key 3: (Ctrl-C): Copy selection to buffer, Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed. 

> - If you can only press the keyboard for N times (with the above four keys), write a program to produce maximum numbers of A's. That is to say, the input parameter is N (No. of keys that you can press), the output is M (No. of As that you can produce).

## Solution
- Time complexity: O(n)
- Space complexity: O(n)

```python
class Solution:
    def keySequencer(N):
    
        # If N is less than 7, the output is itself.
        # Ex: N = 6 (A, A, A, Ctrl-A, Ctrl C, Ctrl V)
        if ( N < 7):
            return N

        # Store the result:
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = [0] * N

        # Initialize the optimal result list for up to 6 key presses.
        # [1, 2, 3, 4, 5, 6, 0, 0, 0, 0, 0]
        for i in range(1, 7): 
            result[i - 1] = i
        
        # If N is greather than 7, calculate M based on i-3, i-4, or i-5 key presses.
        for i in range(7, N + 1): 
            result[i - 1] = max(
                1 * result[i - 3], 
                2 * result[i - 4], 
                3 * result[i - 5], 
                4 * result[i - 6]); 
            
        return result[N - 1]
```