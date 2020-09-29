"""
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
from collections import deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right



def minDepth(root: TreeNode) -> int:
	if not root:
		return 0
	queue = deque()
	queue.append(root)
	min_level = 0
	while queue:
		min_level += 1
		level_size = len(queue)
		for _ in range(level_size):
			node = queue.popleft()
			if not node.left and not node.left:
				return min_level
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)





def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.left.right = TreeNode(2)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Level order traversal: " + str(minDepth(root)))


main()
