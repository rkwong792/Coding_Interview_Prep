# Merge Two Sorted Lists

> - Difficulty: Easy
> - Type: Linked List
> - [link](https://leetcode.com/problems/merge-two-sorted-lists/)

## Solution
- Time complexity: O(m + n) where m and n are the lengths of the two sorted linked lists
- Space complexity: O(1)

```python
class Solution:
    def mergeTwoLists(self, list1, list2):

        dummy = tail = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2

        return dummy.next
```