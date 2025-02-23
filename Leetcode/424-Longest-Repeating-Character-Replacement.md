# Longest Repeating Character Replacement

> - Difficulty: Medium
> - Type: Two Pointers
> - [link](https://leetcode.com/problems/longest-repeating-character-replacement/)

## Solution
- Time complexity: O(N) because each character is processed at most twice (once when expanding right and once when moving left).
- Space complexity: O(1) Space since we only store a small frequency dictionary (at most 26 letters).

- *Hint: Without max_freq (Recalculating Every Time)
Each time the left pointer moves, we would need to recompute the most frequent character in our window by iterating through count, which takes O(26) = O(1) time since there are only uppercase English letters.*

- *With max_freq (Optimized)
We keep track of the most frequent character seen so far and avoid recomputation, keeping our solution strictly O(N).*

```python
class Solution:
    def characterReplacement(s: str, k: int) -> int:
        count = {}  # Dictionary to store frequency of letters
        left = 0
        max_freq = 0  # Most frequent character in the current window
        max_length = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            # If we need to replace more than k characters, shrink the window
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1  # Move left pointer to shrink the window

            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length
```