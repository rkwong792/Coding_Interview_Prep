# Reorder List

> - Difficulty: Medium
> - Type: Linked List
> - [link](https://leetcode.com/problems/reorder-list/)

## Solution
- Time complexity: O(n) - Where n is the size of the linked list
- Space complexity: O(n) - No extra memory.

```python
class Solution:
    def reorderList(self, head):
        # Time Complexity: O(n) - Where n is the size of the linked list
        # Space: O(1) - No extra memory.

        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half (206. Reverse Linked List)
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
```