# Invert Binary Tree

> - Difficulty: Easy
> - Type: Trees
> - [link](https://leetcode.com/problems/invert-binary-tree/)

## Solution
- Time complexity: O(n) - Since each node in the tree is visited only once where 'n' is the # if nodes in the tree.
- Space complexity: O(h) function calls will be placed on the call stack in the worst case, where h is the height of the tree. Because h ∈ O(n), the space complexity is O(n).

```python
class TreeNode:
    # Constructor
    def __init__(self, val = 0, left = None, right = None):
        # Member variables
        self.val = val
        self.left = left
        self.right = right

        # 'self' = 'this'
        # If you want to call a member function from another member function,
        # use 'self.function_name'.

        # You only use the 'self' keyword inside classes.

def invertBinaryTree(root):

    if not root:
        return None

    root.left, root.right = root.right, root.left

    invertBinaryTree(root.left)
    invertBinaryTree(root.right)

    # Return the root once everything is inverted.
    # Note, the root return doesn't matter for the recursive calls as we're not setting the return value
    return root

def preOrderTraversal(root):

    if not root:
        return None

    # End paramater in the print statement is used to add any string at the end of the print output.
    # By default, the print function ends with a newline.
    print(root.val, end = ' ')
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

if __name__ == '__main__':

    ''' Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        4   5   6   7
    '''

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    invertBinaryTree(root)
    preOrderTraversal(root)
```











