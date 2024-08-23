# Add Two Numbers

> - Difficulty: Medium
> - Type: Linked List
> - [link](https://leetcode.com/problems/add-two-numbers/)

## Solution
- Time complexity: 
- Space complexity:
- Singly Linked List

```python
# Insert class definition here:
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# Initialize class here
myObj = Solution()

# Test Cases - Singly Linked List
l1 = ListNode(5, ListNode(6, ListNode(4)))
l2 = ListNode(2, ListNode(4, ListNode(3, ListNode(3))))

node = myObj.addTwoNumbers(l1, l2)

while node:
    print(node.val)
    node = node.next
```