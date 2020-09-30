"""
Problem Statement #
Given a binary tree, connect each node
with its level order successor. The last node of each level should point to a null node.
"""

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



def connect_all_siblings(root):
	if root is None:
		return
	queue = deque()
	queue.append(root)
	while queue:
		previous_node = None
		level_size = len(queue)
		for _ in range(level_size):
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
	connect_all_siblings(root)
	print("Level order traversal")
	root.print_level_order()


main()