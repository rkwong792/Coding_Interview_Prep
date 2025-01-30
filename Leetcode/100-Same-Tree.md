# Same Tree

> - Difficulty: Easy
> - Type: Trees
> - [link](https://leetcode.com/problems/same-tree/)

## Solution
- Time complexity: O(N), where N is a number of nodes in the tree, since one visits each node exactly once.
- Space complexity: O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.

```python
class Solution:
    # DFS - Recursion
    def isSameTree(self, p, q)
        if not p and not q: 
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```