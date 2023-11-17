# Reverse Linked List

> - Difficulty: Easy
> - Type: Linked List
> - [link](https://leetcode.com/problems/reverse-linked-list/)

## Solution
- Time complexity: O(n)
- Space complexity: O(1)

```python
class Solution:
    def reverseList(self, head):
        # Notes:
        # Before 1-> 2-> 3-> 4-> 5 (head starts at 1)
        # After 1 <- 2 <- 3 <- 4 <- 5 (head starts at 5)
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
```