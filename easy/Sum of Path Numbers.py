"""
Problem Statement #
Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path
will represent a number. Find the total sum of all the numbers represented by all paths.
"""

class TreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left= None
		self.right = None


def find_sum_of_path_numbers(root):
	return find_sum_of_path_helper(root, 0)


def find_sum_of_path_helper(node, path_sum):
	if node is None:
		return 0
	path_sum = path_sum*10 + node.val
	if node.left is None and node.right is None:
		return path_sum

	return find_sum_of_path_helper(node.left, path_sum) + find_sum_of_path_helper(node.right, path_sum)


""" 
Path With Given Sequence (medium)

Problem Statement #
Given a binary tree and a number sequence, find if the sequence is present as 
a root-to-leaf path in the given tree.
"""

def find_path(root, sequence):
	if not root:
		return len(sequence) == 0
	return helper(root, sequence, 0)


def helper(node, sequence, sequence_idx):
	if not node:
		return False
	sequence_length = len(sequence)
	if sequence_idx > sequence_length or node.val != sequence[sequence_idx]:
		return False
	if node.left is None and node.right is None and sequence_idx == sequence_length-1:
		return True

	return helper(node.left, sequence,sequence_idx+1) or helper(node.right, sequence, sequence_idx+1)







def main():
	root = TreeNode(1)
	root.left = TreeNode(0)
	root.right = TreeNode(1)
	root.left.left = TreeNode(1)
	root.right.left = TreeNode(6)
	root.right.right = TreeNode(5)
	print("Answer: " + str(find_path(root, [1,0,7])))
	print("Answer: " + str(find_path(root, [1, 1, 6])))

main()
