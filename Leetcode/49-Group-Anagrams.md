# Group Anagrams

> - Difficulty: Medium
> - Type: Arrays & Hashing
> - [link](https://leetcode.com/problems/group-anagrams/)

## Solution
- Time complexity: O(m * n log n) - The sort has a time complexity n log n where n is the average length of the strings.
- Space complexity: O(n) - Hash Map

```python
class Solution:
    def groupAnagrams(self, strs):        
        anagrams = {} # {sortedString, [list of unsorted anagrams]}
        
        for word in strs:

            # "".join() concats all of the characters with nothing "" in between them.
            # Ex: '*'.join(['1', '2'])
            # '1*2'
            # When we sort our string, it returns a list with each character.
            # We have to put the characters back together by using .join()

            sortedString = "".join(sorted(word))
            
            if sortedString not in anagrams:
                anagrams[sortedString] = [word]
            else:
                anagrams[sortedString].append(word)
        
        return anagrams.values()
```