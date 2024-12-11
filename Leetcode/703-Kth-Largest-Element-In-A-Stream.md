# Kth Largest Element in a Stream

> - Difficulty: Easy
> - Type: Heap / Priority Queue
> - [link](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

## Solution
### Time Complexity
- **Initialization**: \( O(n) \)
- **`add()` method**: \( O(log k) \)

### Space Complexity
- **Initialization**: \( O(k) \)
- **`add()` method**: \( O(k) \)


```python
import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        # Create a min-heap with the initial elements
        self.min_heap = nums
        heapq.heapify(self.min_heap)  # Convert the list into a min-heap
        # Keep only the largest k elements
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Push the new value and pop the smallest value in one operation
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            heapq.heappushpop(self.min_heap, val)
        # Return the smallest element in the heap (the kth largest element)
        return self.min_heap[0]

# Example Usage
if __name__ == "__main__":
    # Initialize with k = 3 and nums = [4, 5, 8, 2]
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))  # Output: 4
    print(kthLargest.add(5))  # Output: 5
    print(kthLargest.add(10)) # Output: 5
    print(kthLargest.add(9))  # Output: 8
    print(kthLargest.add(4))  # Output: 8

```