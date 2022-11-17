# 1448. Count Good Nodes in Binary Tree

> - Difficulty: Medium
> - Type: Trees
> - [link](https://leetcode.com/problems/count-good-nodes-in-binary-tree/)

## Solution
- Time complexity: O(n) - Since each node in the tree is visited only once where 'n' is the # if nodes in the tree.
- Space complexity: O(h) function calls will be placed on the call stack in the worst case, where h is the height of the tree. Because h ∈ O(n), the space complexity is O(n).

```python
class Solution:
    def goodNodes(self, root):

        # DFS / Pre-order Traversal

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            return res + dfs(node.left, maxVal) + dfs(node.right, maxVal)

        return dfs(root, root.val)
```