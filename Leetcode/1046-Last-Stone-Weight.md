# Last Stone Weight

> - Difficulty: Easy
> - Type: Heap / Priority Queue
> - [link](https://leetcode.com/problems/last-stone-weight/)

## Solution
- Time complexity: O(n log n)
- Space complexity: O(n)

```python
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # Convert all weights to negative to simulate a max-heap
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(stones) > 1:
            # Pop two heaviest stones
            largest_stone = heapq.heappop(stones)
            second_largest_stone = heapq.heappop(stones)

            # If the stones are not equal, the remainder goes back into the heap
            if largest_stone != second_largest_stone:
                heapq.heappush(stones, largest_stone - second_largest_stone)

        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
```