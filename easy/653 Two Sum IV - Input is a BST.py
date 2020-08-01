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
		d = {}
		while current is not None:
			if k - current.left.val not in d:
				d[current.left.val] = 1
			elif k - current.left.val in d:
				return True
			if k-current.right.val not in d:
				d[current.right.val]=1
			elif k-current.right.val in d:
				return True
		self.findTarget(current.left, k)
		self.findTarget(current.right, k)
		return False


test = Solution()
print(test.findTarget([5,3,6,2,4,None,7], 9))


