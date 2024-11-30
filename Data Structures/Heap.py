import heapq

# You can acess the root of the max/min heap with nums[0] for example. A heap only guarantees that the smallest element (in a min-heap) 
# or largest element (in a max-heap, using negatives) is at the root. The rest of the elements in the list may not be in sorted order.

# Time Complexity of heapq heappush(), heappop(), and heappushpop(): O(log n)
# Where n is the number of elements in the heap before the push operation.

# In a heapified list for max heap solutions, this would take O(log n) where n is the length of nums.
# In a min heap solution, where we only need to heappush k times, this would take O(log k).

# heapq.heappush(heap, item) - Adds the item to the heap while maintaining the heap property.
heap = [1, 3, 5, 7, 9, 2]
heapq.heapify(heap)  # Turn list into a heap
heapq.heappush(heap, 4)  # Add 4 to the heap
print(heap)  # Output: [1, 3, 2, 7, 9, 5, 4]

# heapq.heappop(heap) - Removes and returns the smallest element from the heap.
heap = [1, 3, 5, 7, 9, 2]
heapq.heapify(heap)
smallest = heapq.heappop(heap)  # Removes and returns the smallest element
print(smallest)  # Output: 1
print(heap)  # Output: [2, 3, 5, 7, 9]

# heapq.heappushpop(heap, item) - Pushes an element onto the heap and then pops the smallest element, all in a single atomic operation.
heap = [1, 3, 5, 7, 9, 2]
heapq.heapify(heap)
result = heapq.heappushpop(heap, 4)  # Push 4 and then pop the smallest element
print(result)  # Output: 1 (the smallest element)
print(heap)    # Output: [2, 3, 4, 7, 9, 5]

