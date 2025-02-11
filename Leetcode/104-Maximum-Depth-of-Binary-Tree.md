# Maximum Depth of Binary Tree

> - Difficulty: Easy
> - Type: Trees
> - [link](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Solution
- Time complexity: O(n) - Since each node in the tree is visited only once where 'n' is the # if nodes in the tree.
- Space complexity: O(h) function calls will be placed on the call stack in the worst case, where h is the height of the tree. Because h ∈ O(n), the space complexity is O(n).

```python
class Solution:
    def maxDepth(self, root):
        
        # BFS / Level order traversal
        
        if not root: return 0
        
        level = 0
        q = deque()
        q.append(root)
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
```

## Solution
- Time complexity: O(n) - Since each node in the tree is visited only once where 'n' is the # of nodes in the tree.
- Space complexity: O(h) - The key reason is recursion uses the call stack, and the maximum depth of recursion is the height (h) of the tree.

```python
class Solution:
    def maxDepth(self, root):
        
        # DFS - Recursion
        
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
```