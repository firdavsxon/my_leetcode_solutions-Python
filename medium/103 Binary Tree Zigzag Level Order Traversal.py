"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""
from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def zigzagLevelOrder(root: TreeNode) -> List[List[int]]:
	result = []
	if not root:
		return []
	queue = deque()
	queue.append(root)
	left_to_right = True
	while queue:
		level_size = len(queue)
		current_level = deque()
		for _ in range(level_size):
			current_node = queue.popleft()
			if left_to_right:
				current_level.append(current_node.val)
			else:
				current_level.appendleft(current_node.val)
			if current_node.left:
				queue.append(current_node.left)
			if current_node.right:
				queue.append(current_node.right)
		result.append(list(current_level))
		left_to_right  = not left_to_right
	return result





def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	root.right.left.left = TreeNode(20)
	root.right.left.right = TreeNode(17)
	print("ZigZag traversal: " + str(zigzagLevelOrder(root)))


main()
