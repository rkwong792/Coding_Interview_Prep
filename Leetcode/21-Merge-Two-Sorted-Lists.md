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

        dummy = ListNode()
        current = dummy 
        # dummy is used as a pointer to the beginning of the linked list, while current is used to build out our linked list
        
        # "Shared Reference" in Python
        # 1) Creates an object ListNode
        # 2) Creates variable dummy, and reference to this new object
        # 3) Create variable current, and references the same object that dummy does            

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 or list2

        return dummy.next
```