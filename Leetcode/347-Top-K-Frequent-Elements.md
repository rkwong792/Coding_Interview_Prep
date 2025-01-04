# Top K Frequent Elements

> - Difficulty: Medium
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/top-k-frequent-elements/)

## Min Heap Solution
- Time Complexity: O(n log k)
    - Counting frequencies: 𝑂(𝑛)
    - Heap operations: Each heappush/heappushpop takes 𝑂(log ⁡𝑘). Inserting all n elements takes 𝑂(𝑛 log 𝑘)
    - Extracting k elements: O(k log k)
    - Total Time Complexity: O(n + n log k + k log k) = O(n log k)

- Space Complexity: O(n + k)
- Dictionary = O(n)
- Heap = O(k)

```python
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

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
```




## Max Heap Solution
- Time Complexity: O(n log n)
    - Counting frequencies: 𝑂(𝑛)
    - Building the heap with all n elements: 𝑂(𝑛 log ⁡𝑛)
    - Extracting k elements: 𝑂(𝑘 log ⁡𝑛)
    - Total Time Complexity: O(n + n log n + k log n) = O(n log n)

- Space Complexity: O(n)

```python
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            count[num] = count.get(num,0) + 1

        min_heap = []

        for num, freq in count.items():
            heapq.heappush(min_heap, (-freq, num))
        
        res = []
        for _ in range(k):
            res.append(heapq.heappop(min_heap)[1])
        
        return res
```

## Bucket Sort Solution
- Time complexity: O(n) - Need to loop through the the entire list in reverse order in O(N) and also the nested list in O(N) time. 
- Space complexity: O(n) - We need O(n) space for our hash map and also O(N) space for our list[[]]. O(n) + O(n) = O(N)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # +1 is important for nums=[1], k=1 edge case
        freq = [[] for i in range(len(nums)+1)]
        
        count = {}
        
        for num in nums:
            count[num] = count.get(num,0) + 1
            
        for v, f in count.items():
            freq[f].append(v)
            
        res = []
        
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
```