# Merge k Sorted Lists

> - Difficulty: Hard
> - Type: Heap / Priority Queue
> - [link](https://leetcode.com/problems/merge-k-sorted-lists/)

## Solution
- Time complexity: O(n log k), where n is the total # of nodes across all k lists, k is the number of lists
- Space complexity: O(k)

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # Min-heap to store the nodes, sorted by their value
    min_heap = []

    # k log k
    # Step 1: Push the first node of each list into the min-heap
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))

            # Tuple Explanation:
            # 1) The value of the current node. This is the key used to order elements in the heap. The heapq module automatically organizes the heap based on the first element of the tuple (smallest node.val comes to the top).
            # 2) The index of the list that the node belongs to. This ensures that two nodes with the same value can still be distinguished in the heap.
            # 3) The actual node object itself, so we can advance the pointer in its list after popping it from the heap.

    dummy = ListNode()
    current = dummy

    # Step 2: Extract nodes and add to the merged list we're building
    # n log k
    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = node # Add the smallest node to the merged list
        current = current.next # Move the `current` pointer forward
        node = node.next # Advance to the next node in the same list
        if node:
            heapq.heappush(min_heap, (node.val, i, node))
    
    return dummy.next
```