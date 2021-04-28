"""
Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

Example

For

t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": null,
                "right": null
            },
            "right": {
                "value": -3,
                "left": null,
                "right": null
            }
        }
    }
}
and
s = 7,
the output should be hasPathWithGivenSum(t, s) = true.

This is what this tree looks like:

      4
     / \
    1   3
   /   / \
  -2  1   2
    \    / \
     3  -2 -3
Path 4 -> 3 -> 2 -> -2 gives us 7, the required sum.

For

t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": {
                "value": -4,
                "left": null,
                "right": null
            },
            "right": {
                "value": -3,
                "left": null,
                "right": null
            }
        }
    }
}
and
s = 7,
the output should be hasPathWithGivenSum(t, s) = false.

This is what this tree looks like:

      4
     / \
    1   3
   /   / \
  -2  1   2
    \    / \
     3  -4 -3
There is no path from root to leaf with the given sum 7.

Input/Output

[execution time limit] 4 seconds (py)

[input] tree.integer t

A binary tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 5 · 104,
-1000 ≤ node value ≤ 1000.

[input] integer s

An integer.

Guaranteed constraints:
-4000 ≤ s ≤ 4000.

[output] boolean

Return true if there is a path from root to leaf in t such that the sum of node values in it is equal to s, otherwise return false.

"""


#
# Binary trees are already defined with this interface:
class Tree(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


from collections import deque

def hasPathWithGivenSum(root, s):
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

# def dfs(node, summa, s):
# 	current = node
# 	while current:
# 		summa += current.value
# 		if summa == s:
# 			return summa
# 		if current.left:
# 			current = current.left
# 			dfs(current.left, summa, s)
# 		elif current.right:
# 			current = current.right
# 			dfs(current.right, summa, s)
# 	return False


t = Tree(4)
t.left = Tree(1)
t.right = Tree(3)
t.left.left = Tree(-2)
t.right.right = Tree(2)
t.right.left = Tree(1)
t.left.left.right = Tree(3)
t.right.right.left = Tree(-2)
t.right.right.right = Tree(-3)

print(hasPathWithGivenSum(t, s=7))
