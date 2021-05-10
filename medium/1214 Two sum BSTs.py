"""
Given the roots of two binary search trees, root1 and root2, return true if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer target.



Example 1:


Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.
Example 2:


Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
Output: false

"""


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
		r1 = []
		r2 = []

		def traverse(root, lst):
			if not root:
				return lst
			lst.append(root.val)
			if root.left:
				traverse(root.left, lst)
			if root.right:
				traverse(root.right, lst)
			return lst

		ro1 = traverse(root1, r1)
		ro2 = traverse(root2, r2)
		for i in ro1:
			if target - i in ro2:
				return True
		return False


root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(4)

root2 = TreeNode(1)
root2.left = TreeNode(0)
root2.right = TreeNode(3)





test = Solution()
print(test.twoSumBSTs(root1, root2, target=5))
