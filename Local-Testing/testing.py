# Merge two sorted lists

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# Create list1 and list2 singly linked lists
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

def mergeTwoLists(list1, list2):
    head = ListNode()
    current = head

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return head.next

# Helper function to print the linked list
def printLinkedList(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(" -> ".join(map(str, values)))


printLinkedList(mergeTwoLists(list1, list2))
