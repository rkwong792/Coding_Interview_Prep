import heapq

nums = [3,2,1,5,6,4]
k = 2

def findKthLargest(nums, k) -> int:
    
    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappushpop(min_heap, num)
    print(min_heap[1])

    return min_heap[0]

findKthLargest(nums, k)

# time: O(N * log n)
# space: O(k)