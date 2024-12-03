# Sample class
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

# Helper function to print the linked list
def printLinkedList(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))

printLinkedList(list1)