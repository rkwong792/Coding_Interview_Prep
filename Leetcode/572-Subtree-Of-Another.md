# 572. Subtree of Another Tree

> - Difficulty: Easy
> - Type: Trees
> - [link](https://leetcode.com/problems/subtree-of-another-tree/)

## Solution
- Time complexity: O(M * N) - Sizes of both trees multiplied together.
- Space complexity: O(M + N) - Sizes of both trees added together.

```python
class Solution(object):
    # DFS Solution - 

    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def isSameTree(self, s, t):
        if not s and not t:
            return True
        
        if not s or not t:
            return False
        
        if s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
```