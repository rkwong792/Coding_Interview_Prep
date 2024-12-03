#

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

list1 = ListNode(4)
list1.next = ListNode(5)
list1.next.next = ListNode(2)

# print the linked list
def printLinkedList(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    
    print(" --> ".join(map(str, values)))
              
print(printLinkedList(list1))