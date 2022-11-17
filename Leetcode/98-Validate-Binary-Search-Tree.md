# 98. Validate Binary Search Tree

> - Difficulty: Medium
> - Type: Trees
> - [link](https://leetcode.com/problems/validate-binary-search-tree/)

## Solution
- Time complexity: O(n) - Since each node in the tree is visited only once where 'n' is the # if nodes in the tree.
- Space complexity: O(h) function calls will be placed on the call stack in the worst case, where h is the height of the tree. Because h ∈ O(n), the space complexity is O(n).

```python
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # Lower / Upper Bound
        def valid(node, lower, upper):
            if not node:
                return True
            
            if not (node.val > lower and node.val < upper):
                return False
            
            return valid(node.left, lower, node.val) and valid(node.right, node.val, upper)


        return valid(root, float('-inf'), float('inf'))
```