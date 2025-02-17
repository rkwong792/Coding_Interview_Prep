# 98. Validate Binary Search Tree

> - Difficulty: Medium
> - Type: Trees
> - [link](https://leetcode.com/problems/validate-binary-search-tree/)

## Solution
- Time complexity: O(n) - Since each node in the tree is visited only once where 'n' is the # if nodes in the tree.
- Space complexity: O(h) function calls will be placed on the call stack in the worst case, where h is the height of the tree. Because h ∈ O(n), the space complexity is O(n).

```python
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, min_val, max_val):
            if not node:
                return True  # Base case: Empty tree is always valid
            
            if not (min_val < node.val < max_val):
                return False  # If the node violates BST rules, return False
            
            # Check left subtree (values must be less than current node)
            left_valid = dfs(node.left, min_val, node.val)
            
            # Check right subtree (values must be greater than current node)
            right_valid = dfs(node.right, node.val, max_val)
            
            return left_valid and right_valid  # Both subtrees must be valid

        return dfs(root, float("-inf"), float("inf"))  # Start with infinite range

```