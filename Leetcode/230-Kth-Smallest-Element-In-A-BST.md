# 230. Kth Smallest Element in a BST

> - Difficulty: Medium
> - Type: Trees
> - [link](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

## Solution
- Time complexity: O(H + k)
- Space complexity: O(h) function calls will be placed on the call stack in the worst case, where h is the height of the tree. Because h ∈ O(n), the space complexity is O(n).

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        curr = root
        
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
```

## Solution
- Time complexity: O(N)
- Space complexity: O(h) - Recursive stack

```python
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k  # Counter for kth element
        self.result = None  # Store kth smallest element
        
        def inorder(node):
            if not node or self.result is not None:
                return
            
            inorder(node.left)  # Traverse left subtree
            
            self.k -= 1
            if self.k == 0:
                self.result = node.val  # Found kth smallest
                return
            
            inorder(node.right)  # Traverse right subtree
        
        inorder(root)
        return self.result
```