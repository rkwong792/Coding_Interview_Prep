class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
# Write a function to calculate the Maximum Depth of Binary Tree
'''
        3
       / \
      9   20
          / \
        15   7

'''

def preOrderTraversal(root):
    if not root:
        return
    # print node -> left -> right

    # End paramater in the print statement is used to add any string at the end of the print output.
    # By default, the print function ends with a newline.
    print(root.val, end = ' ')
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def maxDepth(root):
    # use recursion - post order. left -> right -> root
    if not root:
        return 0
    
    left_height = maxDepth(root.left)
    right_height = maxDepth(root.right)

    return 1 + max(left_height, right_height)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

preOrderTraversal(root)
print(maxDepth(root))





