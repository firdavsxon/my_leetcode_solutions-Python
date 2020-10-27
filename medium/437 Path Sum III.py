"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf,
but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the
range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def pathSum(self, root: TreeNode, sum: int) -> int:
		def dfs(root, summa):
			nonlocal num
			if not root:
				return

			summa += root.val
			if summa == k:
				num += 1

			num += h[summa - k]
			h[summa] += 1

			dfs(root.left, summa)
			dfs(root.right, summa)
			h[summa] -= 1

		num, k = 0, sum
		h = defaultdict(int)
		dfs(root, 0)
		return num


test = Solution()
# root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
root= TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(1)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)
print(test.pathSum(root, 8))
