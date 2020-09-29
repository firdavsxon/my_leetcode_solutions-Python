"""
Given a non-empty binary tree, return the average value of the
nodes on each level in the form of an array.
Example 1:
Input:
	3
   / \
  9  20
	/  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11.
 Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
"""
from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
def averageOfLevels(root: TreeNode) -> List[float]:
	result = []
	if not root:
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
		median = sum(current_level)/len(current_level)
		result.append(median)
	return result



def main():
	root = TreeNode(12)
	root.left = TreeNode(7)
	root.right = TreeNode(1)
	root.left.left = TreeNode(9)
	root.left.right = TreeNode(2)
	root.right.left = TreeNode(10)
	root.right.right = TreeNode(5)
	print("Level order traversal: " + str(averageOfLevels(root)))


main()

