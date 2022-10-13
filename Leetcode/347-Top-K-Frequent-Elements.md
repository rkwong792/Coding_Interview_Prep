# Top K Frequent Elements

> - Difficulty: Medium
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/top-k-frequent-elements/)

## Solution
- Time complexity: O(N) - Need to loop through the the entire list in reverse order in O(N) and also the nested list in O(N) time. 
- Space complexity: O(N) - We need O(N) space for our hash map and also O(N) space for our list[[]]. O(N) + O(N) = O(N)

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                
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