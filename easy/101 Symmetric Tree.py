"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Follow up: Solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:

	def isSymmetric(self, root: TreeNode) -> bool:
		if not root:
			return True
		return self.isMirror(root, root)

	def isMirror(self, left, right):

		if left is None and right is None:
			return True
		if left is None or right is None:
			return False

		if left.val == right.val:
			inpair = self.isMirror(left.right, right.left)
			outpair = self.isMirror(left.left, right.right)

			return outpair and inpair
		return False