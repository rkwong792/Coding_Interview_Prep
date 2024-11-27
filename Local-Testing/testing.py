import heapq

nums = [1,1,1,2,2,3,7,7,7,7,7]
k = 2

def topKFrequentElements(nums, k):

    # use a max heap

    # use a min heap
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    min_heap = []

    for num, freq in count.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        else:
            heapq.heappushpop(min_heap, (freq, num))
    
    res = []
    for _ in range(k):
        res.append(heapq.heappop(min_heap)[1])

    return res

print(topKFrequentElements(nums, k))