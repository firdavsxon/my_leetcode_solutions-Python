"""
Problem Statement #
Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right
 in separate sub-arrays.
Example1:

[ 	[1],
   [2,3],
  [4,5,6,7]  ]

"""
from collections import deque


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def traverse(root):

	result = []
	if root is None:
		return result

	queue = deque()
	queue.append(root)
	while queue:
		level_size = len(queue)
		current_level = []
		for _ in range(level_size):
			current_node = queue.popleft()
			current_level.append(current_node.val)
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)
		result.append(current_level)

	return result

def tra(root):
	result = deque()
	if root is None:
		return result

	queue = deque()
	queue.append(root)

	while queue:
		level_size = len(queue)
		current_level_array = []
		for _ in range(level_size):
			current_node = queue.popleft()
			current_level_array.append(current_node.val)
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)
		result.appendleft(current_level_array)
	return result

def zig_zag(root):
	result = deque()
	if root is None:
		return []

	queue = deque()
	queue.append(root)
	switch = True
	while queue:
		level_zie = len(queue)
		current_level = deque()
		for _ in range(level_zie):
			current_node = queue.popleft()
			if switch:
				current_level.append(current_node.val)
			else:
				current_level.appendleft(current_node.val)
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)

		result.append(current_level)
		switch = not switch
	return result


def min_depth(root):
	result = 0
	if not root:
		return 0
	queue = deque()
	queue.append(root)

	while queue:
		result += 1
		level_length = len(queue)
		for _ in range(level_length):
			current_node = queue.popleft()

			if current_node.left is None and current_node.right is None:
				return result

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
	root.right.left.left = TreeNode(11)
	print("Level order traversal: " + str(min_depth(root)))


main()
