import heapq

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)
lists = [list1, list2, list3]

def printLinkedList(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    print("->".join(map(str, values)))
              

def mergeKLists(lists):
    # use min-heap
    min_heap = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        node = node.next
        if node:
            heapq.heappush(min_heap, (node.val, i, node))
    
    return dummy.next



printLinkedList(mergeKLists(lists))

# 1->1->2->3->4->4->5->6
