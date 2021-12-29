"""
Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

  1
  2
  3
  4
  5
  6
  7
 Example 1
 Right View: [1, 3, 7]
 Exampe 2
 Right View: [12, 1, 5, 3]
  12
  7
  1
  9
  3
  10

"""

from __future__ import print_function
from collections import deque


class TreeNode:

	def __init__(self, val):
		self.val = val
		self.left, self.right, self.next = None, None, None

class Solution:

	def tree_right_view(self, root):
		result = []
		if not root:
			return []

		queue = deque([root])
		while queue:
			level = len(queue)
			for i in range(level):
				current_node = queue.popleft()
				if i == level-1:
					result.append(current_node)
				if current_node.left:
					queue.append(current_node.left)
				if current_node.right:
					queue.append(current_node.right)
		return result




def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	solution = Solution()
	result = solution.tree_right_view(root)
	for node in result:
		print(str(node.val) + " ", end='')


main()