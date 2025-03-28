# Sort Array by Increasing Frequency

> - Difficulty: Easy
> - Type: Arrays & Hashing
> - [link](https:///sort-array-by-increasing-frequency/)

## Solution
- Time complexity: O(n log n) - Sorting Dominates
 - Space complexity: O(n)

```python
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        nums.sort(key=lambda n: (count[n], -n))

        return nums
```