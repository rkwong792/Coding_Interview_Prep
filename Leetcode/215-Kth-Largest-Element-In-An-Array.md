# Kth Largest Element in an Array

> - Difficulty: Medium
> - Type: Heap / Priority Queue
> - [link](https://leetcode.com/problems/kth-largest-element-in-an-array/)

## Solution
- Assuming K << N (Assuming K much less than N)
- O(N) - negating all elements
- O(N) - heapifying the list 
- O(K log N) - popping K times, each pop is log N
- Final heappop - O(log N)
- `Total Time Complexity: O(N + K log N)`

- `Space complexity: O(1)`
- The heap is stored in place, and the input list nums is modified in place (no extra space is required for storing the heap).

```python
import heapq

class Solution:
     # Max Heap Solution
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Max Heap of size N
        # Time: O(N + k log N)
        # Space: O(1)

        for i in range(len(nums)):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)
```


## Solution
- `Time complexity: O(N * log k)`
- The loop runs for n elements, and for each element, we perform a heap operation (heappush or heappushpop), each of which takes O(log k) time. Each heappushpop() operation takes O(log k), and you perform it n times, giving O(n log k).

- `Space complexity: O(k)`
- The space complexity comes from storing the min_heap, which at most contains k elements. This is because the heap will contain only the 𝑘 largest elements in the array at any given point.

```python
import heapq

class Solution:
     # Min Heap Solution
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # Min Heap Solution
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)
        
        return min_heap[0]
```