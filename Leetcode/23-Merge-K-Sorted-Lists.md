# Merge k Sorted Lists

> - Difficulty: Hard
> - Type: Heap / Priority Queue
> - [link](https://leetcode.com/problems/merge-k-sorted-lists/)

## Solution
- Time complexity: 
- Space complexity:

```python
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # To use ListNode in a min-heap, we need to define comparison methods.
    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists):
    # Min-heap to store the nodes, sorted by their value
    min_heap = []

    # Step 1: Push the first node of each list into the min-heap
    for l in lists:
        if l:
            heapq.heappush(min_heap, l)

    # Dummy node to help simplify the list concatenation
    dummy = ListNode(0)
    current = dummy

    # Step 2: Extract nodes and add the next node from the same list
    while min_heap:
        # Get the smallest node from the heap
        node = heapq.heappop(min_heap)
        current.next = node
        current = current.next  # Move the pointer to the last node

        # If the node has a next node, push it into the heap
        if node.next:
            heapq.heappush(min_heap, node.next)

    return dummy.next
```


```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        h = []

        for i, l in enumerate(lists):
            if l:
                heappush(h, (l.val,i))
        
        dummy = curr = ListNode(0)

        while h:
            val, i = heappop(h)
            curr.next = ListNode(val)

            if lists[i].next:
                heappush(h, (lists[i].next.val,i))
                lists[i] = lists[i].next
            curr = curr.next
        
        return dummy.next
```