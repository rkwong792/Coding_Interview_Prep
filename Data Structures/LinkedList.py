# Helper function to print the linked list
def printLinkedList(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print(" -> ".join(map(str, values)))