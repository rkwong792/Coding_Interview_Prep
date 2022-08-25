# Remove Nth Node From End of List

> - Difficulty: Medium
> - Type: Linked List
> - [link](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## Solution
- Time complexity: O(n) - Two pointers
- Space complexity: O(1) - Two pointers

```python
class Solution:
    def removeNthFromEnd(self, head, n):
        
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next
```