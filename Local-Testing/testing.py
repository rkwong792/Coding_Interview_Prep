class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Construct the tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.left.right = TreeNode(6)  # 6 is the right child of 3
root.left.right.left = TreeNode(4)  # 4 is the left child of 6

def kthSmallest(root, k):
    stack = []
    curr = root

    while True:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        
        curr = curr.right

print(kthSmallest(root, 5))


