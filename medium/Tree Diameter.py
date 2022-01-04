"""

Given a binary tree, find the length of its diameter. The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. The diameter of a tree may or may not pass through the root.

Note: You can always assume that there are at least two leaf nodes in the given tree.

 Example 1:
  1
  2
  3
  4
  5
  6
 Output: 5Explaination: The diameter of the tree is: [4, 2, 1, 3, 6]
 Example 2:
  1
  2
  3
  5
  6
  7
  8
  10
  9
  11
"""


class TreeNode:

	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class TreeDiametr:

	def __init__(self):
		self.tree_diametr = 0
		self.tree_max_sum = 0

	def find_diametr(self, root):
		if not root:
			return 0
		self.dfs(root)
		return self.tree_diametr

	def dfs(self, root):
		if not root:
			return 0
		max_left = self.dfs(root.left)
		max_right = self.dfs(root.right)

		diametr = max_left+max_right +1
		self.tree_diametr = max(self.tree_diametr, diametr)
		return max(max_left, max_right) + 1

	def max_path_sum(self, root):
		if not root:
			return 0
		self.dfs_1(root)
		return self.tree_max_sum

	def dfs_1(self, root):
		if not root:
			return 0
		max_left = self.dfs_1(root.left)
		max_right = self.dfs_1(root.right)

		max_sum = max_left+max_right +root.val
		self.tree_max_sum = max(self.tree_max_sum, max_sum)
		return max(max_left, max_right) + root.val



	def inorder_print(self, root):
		if root:
			self.inorder_print(root.left)
			print(root.val)
			self.inorder_print(root.right)




def main():
	tree_diametr = TreeDiametr()
	root = TreeNode(1)
	root.left = TreeNode(2)
	root.right = TreeNode(3)
	root.left.left = TreeNode(1)
	root.left.right = TreeNode(3)
	root.right.left = TreeNode(5)
	root.right.right = TreeNode(6)
	print("Tree Diametr: " + str(tree_diametr.find_diametr(root)))
	# root.left.left  = None
	root.right.left.left = TreeNode(7)
	root.right.left.right = TreeNode(8)
	root.right.right.left = TreeNode(9)
	# root.right.left.right.left = TreeNode(10)
	# root.right.right.left.left = TreeNode(11)
	print("Tree Diametr: " + str(tree_diametr.find_diametr(root)))
	print("Tree Max sum: " + str(tree_diametr.max_path_sum(root)))

main()
