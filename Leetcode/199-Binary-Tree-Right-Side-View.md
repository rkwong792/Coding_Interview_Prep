# 199. Binary Tree Right Side View

> - Difficulty: Medium
> - Type: Trees
> - [link](https://leetcode.com/problems/binary-tree-right-side-view/)

## Solution
- Time complexity: O(n) - Since each node in the tree is visited only once where 'n' is the # if nodes in the tree.
- Space complexity: O(h) function calls will be placed on the call stack in the worst case, where h is the height of the tree. Because h ∈ O(n), the space complexity is O(n).

```python
class Solution:
    def rightSideView(self, root):
        
        # BFS / Level Order Traversal

        q = deque()
        if root:
            q.append(root)
        
        res = []
        while q:
            res.append(q[-1].val)

            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res
```