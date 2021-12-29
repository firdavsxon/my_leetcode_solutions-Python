"""
Problem Statement #
Given a binary tree, connect each node with its level order successor. The last node of each level should point to a null node.

Example 1:

  1
  2
  3
  4
  5
  6
  7
 null
 null
 null
Example 2:

     12 ->  null
    7   1 ->  null
  9    10  5  -> null


"""

from __future__ import print_function

from collections import deque


class TreeNode:

	def __init__(self, val):
		self.val = val
		self.left, self.right, self.next = None, None, None

	def print_level_order(self):
		next_level_root = self
		while next_level_root:
			current = next_level_root
			next_level_root = None
			while current:
				print(str(current.val) + " ", end='')
				if not next_level_root:
					if current.left:
						next_level_root = current.left
					elif current.right:
						next_level_root = current.right
				current = current.next
			print()


class Solution:

	def connect_level_order_siblings(self, root):

		if not root:
			return ""

		queue = deque([root])
		while queue:
			previous_node = None
			level = len(queue)
			for _ in range(level):
				current_node = queue.popleft()
				if previous_node:
					previous_node.next = current_node
				previous_node = current_node
				if current_node.left:
					queue.append(current_node.left)
				if current_node.right:
					queue.append(current_node.right)

	def connect_all_siblings(self, root):
		if not root:
			return  ""

		queue = deque()
		queue.append(root)
		previous_node, current_node = None, None
		while queue:
			current_node = queue.popleft()
			if previous_node:
				previous_node.next = current_node
			previous_node = current_node
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)






def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	solution = Solution()
	solution.connect_all_siblings(root)

	print("Level order traveling using 'next' pointer")

	root.print_level_order()


main()