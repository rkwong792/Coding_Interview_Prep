# Linked List Cycle

> - Difficulty: Easy
> - Type: Linked List
> - [link](https://leetcode.com/problems/linked-list-cycle/)

## Solution
- Time complexity: O(n) - Where n is the length of the linked list.
- Space complexity: O(1)

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```