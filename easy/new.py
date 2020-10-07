class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.right = right
        self.left= left

def dfs(root):
    if not root:
        return

    if root.left:
        dfs(root.left)

    if root.right:
        dfs(root.right)
    print(root.val)

def main():
    root = TreeNode(10)
    root.left = TreeNode(7)
    root.right = TreeNode(15)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(9)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(16)

    print("Printing nodes: ")
    dfs(root)


""" 
                10
                /\
               7    15
              /\    /\
             6  9  12 16
               
"""
main()