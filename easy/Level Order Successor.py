"""
Problem Statement #
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.

Example 1:

 Given Node: 3
 Level Order Successor: 4
							  1
							 | \
							 2   3
						    | \
    					   4   5

"""
from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def find_successor(root, key):
	if not root:
		return None
	queue = deque()
	queue.append(root)
	while queue:
		node = queue.popleft()
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)

		if node.val == key:
			break
	return queue[0].val if queue else None


def level_order_successor(root, key):
	if not root:
		return []
	queue = deque()
	queue.append(root)

	while queue:
		current_node = queue.popleft()
		if current_node.left:
			queue.append(current_node.left)
		if current_node.right:
			queue.append(current_node.right)
		if current_node.val == key:
			break
	return queue[0].val if queue else None

def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Level order traversal: " + str(level_order_successor(root, 9)))


main()
