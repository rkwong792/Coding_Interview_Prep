# Permutation in String

> - Difficulty: Medium
> - Type: Sliding Window
> - [link](https://leetcode.com/problems/permutation-in-string/)

## Solution
- Time complexity: O(N)
- Space complexity: O(1)
- *Hint: Since the problem only involves lowercase English letters (a–z), we can store frequencies in a list of size 26, instead of using a dictionary. With a dictionary (Counter), comparing frequency maps takes O(k) time where k is the # of unique characters in s1. With an array of size 26, comparison is instant (O(1)*

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1

        if s1_counts == s2_counts:
            return True

        for i in range(len(s1), len(s2)):
            s2_counts[ord(s2[i]) - 97] += 1
            s2_counts[ord(s2[i - len(s1)]) - 97] -= 1
            if s1_counts == s2_counts:
                return True

        return False
```