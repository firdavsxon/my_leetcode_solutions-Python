"""
Problem Statement #
Given a binary tree and a number ‘S’, find all paths from
root-to-leaf such that the sum of all the node values of each path equals ‘S’.
"""

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def find_path(root, sum):
	all_path = []
	def helper(current_node, sum, current_path, all_path):
		if current_node is None:
			return
		current_path.append(current_node.val)

		if current_node.val == sum and current_node.left is None and current_node.right is None:
			all_path.append(list(current_path))
		else:
			helper(current_node.left, sum - current_node.val, current_path, all_path)
			helper(current_node.right, sum - current_node.val, current_path, all_path)
		del current_path[-1]
	helper(root, sum, [], all_path)
	return all_path


def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(4)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	sum = 23
	print("Tree path with sum " + str(sum) + ":" + str(find_path(root, sum)))
	sum = 16
	print("Tree path with sum " + str(sum) + ":" + str(find_path(root, sum)))


main()