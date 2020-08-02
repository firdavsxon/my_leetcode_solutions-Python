"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def findTarget(self, root: TreeNode, k: int):
		current = root
		stack = []
		stack1 = []
		d = {}
		while True:
			if current is not None:
				stack.append(current)
				current = current.left
			elif stack:
				current = stack.pop()
				stack1.append(current.val)
				current = current.right
			else:
				break
		for i in stack1:
			if k - i not in d:
				d[i] = 1
			else:
				return True
		return False

# other peoples algorithm
	def findTarget1(self, root: TreeNode, k: int) -> bool:
		if not root:
			return None

		seen = set()

		def helper(node):
			if k - node.val in seen:
				return True
			seen.add(node.val)

			if node.left and helper(node.left):
				return True
			if node.right and helper(node.right):
				return True
			return False

		return helper(root)

	# Brute force, go through all nodes in the tree, adding to a set
	# If target - currNode in seen, return True
	# Else if tree is exhausted, return False
test = Solution()
print(test.findTarget([5,3,6,2,4,None,7], 9))


