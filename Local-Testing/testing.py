# Insert class definition here:
from typing import List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head # head is used as a pointer to the beginning of the linked list, while cur is used to build out our linked list

        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            cur.next = ListNode(val % 10) # Python uses floor division (rounds down)

            # calculate carry
            carry = val // 10

            # update ptrs
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # Final edge case
        if carry:
            cur.next = ListNode(carry)

        return head.next


# Initialize class here
myObj = Solution()

# Test Cases - Singly Linked List
l1 = ListNode(9, ListNode(6, ListNode(4)))
l2 = ListNode(9, ListNode(4, ListNode(3, ListNode(3))))

node = myObj.addTwoNumbers(l1, l2)

while node:
    print(node.val)
    node = node.next