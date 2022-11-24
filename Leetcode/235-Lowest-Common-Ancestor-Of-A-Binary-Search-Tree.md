# 235. Lowest Common Ancestor of a Binary Search Tree

> - Difficulty: Medium
> - Type: Trees
> - [link](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

## Solution
- Time complexity: O(H - We only have to visit one node for every single level in the tree. The time complexity is the height of the tree.
- Space complexity: O(1) - No data structures needed.

```python
class Solution:

    # Iterative Implementation

    def lowestCommonAncestor(self, root, p, q):
        
        curr = root
        while curr:
            # If both p and q are greater than the root, go down right subtree
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            # If both p and q are smaller than the root, go down left subtree
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            # if a split to the left & right occurs, return the current node
            else:
                return curr
```