# Majority Element

> - Difficulty: Easy
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/majority-element/)

## Solution 1 - Linear Space O(N)
- Time complexity: O(N)
- Space complexity: O(N)

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        count = 0
        candidate = None
        for key, value in count.items():
            if value > count:
                count = value
                candidate = key
        
        return candidate
```


## Solution 2 - Constant Space O(1)
- Time complexity: O(N)
- Space complexity: O(1)
- *Hint: Boyer-Moore Majority Vote Algorithm*

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num   # Choose the current number as a new candidate
                
            # Increase if it's the candidate, decrease otherwise
            if num == candidate: 
                count+=1
            else:
                count-=1
        
        return candidate
```

## Verify the candidate
```python
    count = 0
    for num in nums:
        if num == candidate:
            count += 1

    # Return only if it's truly a majority
    if count > len(nums) // 2:
        return candidate
    else:
        return None  # No majority element exists
```