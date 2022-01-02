"""
Problem Statement #
Given a binary tree and a number ‘S’,
find if the tree has a path from root-to-leaf such that the
sum of all the node values of that path equals ‘S’.
"""

class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def has_path(root, sum):
	if root is None:
		return False

	if root.val == sum and root.left is None and root.right is None:
		return True

	return has_path(root.left, sum - root.val) or has_path(root.right, sum - root.val)

def has_sum(root, sum_num):
	if not root:
		return False
	if dfs(root, 0, sum_num):
		return True
	return False


def dfs(root, num, sum_num, all_sum):
	if not root:
		return
	if root:
		num += root.val
	if root.left is None and root.right is None and num == sum_num:
		all_sum.append(1)
		return
	dfs(root.left, num, sum_num, all_sum)
	dfs(root.right, num, sum_num, all_sum)


def all_paths(node, s):
	all_sum = []
	if not node:
		return 0
	dfs(node, 0, s, all_sum)
	return len(all_sum)


def total_sum_binary(root):
	total_summa = []
	if not root:
		return 0
	dfs_total(root, 0, total_summa)
	return sum(total_summa)


def dfs_total(root, current, summa):
	if not root:
		return
	if root:
		current = 10*current + root.val
	if root.left is None and root.right is None:
		summa.append(current)

	dfs_total(root.left, current, summa)
	dfs_total(root.right, current, summa)


def binary_tree_seq(root, sequence):
	if not root:
		return False
	if binary_seq(root, [], sequence):
		return True
	return False

def binary_seq(root, current, sequence):
	if not root:
		return False
	if root:
		current.append(root.val)
	if root.left is None and root.right is None:
		if current == sequence:
			return True
		elif current != sequence:
			while len(current)!=1:
				current.pop()
			return False
	return binary_seq(root.left, current, sequence) or binary_seq(root.right, current, sequence)


def count_path(root, num):
	result = []
	if not root:
		return 0
	dfs_path_sub_sum(root, num, result)


def dfs_path_sub_sum(root, num, result):
	if not root:
		return
	if root:


def main():
	root = TreeNode(10)
	root.left = TreeNode(5)
	root.right = TreeNode(4)
	root.left.left = TreeNode(3)
	root.left.right = TreeNode(11)
	root.right.left = TreeNode(23)
	root.right.right = TreeNode(8)

	print("Tree has path: " + str(total_sum_binary(root)))
	print("Tree has path: " + str(binary_tree_seq(root, [10, 5, 3])))


main()