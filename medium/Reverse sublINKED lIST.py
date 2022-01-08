"""
Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed (See Example 2 for clarification).

Example 1:

Input:
LinkedList: 1->2->2->4->5->6->7->8
K = 4
Output: 4 2 2 1 8 7 6 5
Explanation:
The first 4 elements 1,2,2,4 are reversed first
and then the next 4 elements 5,6,7,8. Hence, the
resultant linked list is 4->2->2->1->8->7->6->5.
Example 2:

Input:
LinkedList: 1->2->3->4->5
K = 3
Output: 3 2 1 5 4
Explanation:
The first 3 elements are 1,2,3 are reversed
first and then elements 4,5 are reversed.Hence,
the resultant linked list is 3->2->1->5->4.
Your Task:
You don't need to read input or print anything. Your task is to complete the function reverse() which should reverse the linked list in group of size k and return the head of the modified linked list.

Expected Time Complexity : O(N)
Expected Auxilliary Space : O(1)

Constraints:
1 <= N <= 104
1 <= k <= N
"""


def print_root(root):
	current = root
	while current:
		print(current.val, end=' -> ')
		current = current.next
	return


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.next = None


class Solution:

	def reverse_linked_list(self, root_node, num):
		current = root_node
		ktail = None
		prev = None
		while current:
			count = 0
			current = root_node
			while count<num and current:
				current = current.next
				count+=1
			if count == num:
				reversed_root = self.reverse_list(root_node, num)
				if not prev:
					prev = reversed_root
				if ktail:
					ktail.next = reversed_root
				ktail = root_node
				root_node = current
		if ktail:
			ktail.next = root_node
		return prev if prev else root_node


	def reverse_list(self, root_node, num):
		prev, current = None, root_node
		while num:
			temp = current.next
			current.next = prev
			prev = current
			current = temp
			num-=1
		return prev


def main():
	root = TreeNode(1)
	root.next = TreeNode(2)
	root.next.next = TreeNode(3)
	root.next.next.next = TreeNode(4)
	root.next.next.next.next = TreeNode(5)
	root.next.next.next.next.next = TreeNode(6)
	root.next.next.next.next.next.next = TreeNode(7)
	root.next.next.next.next.next.next.next = TreeNode(8)
	root.next.next.next.next.next.next.next.next = TreeNode(9)
	root.next.next.next.next.next.next.next.next.next = TreeNode(10)
	root.next.next.next.next.next.next.next.next.next.next = TreeNode(11)

	solution = Solution()
	print_root(root)
	solution.reverse_linked_list(root_node=root, num=10)
	print()
	print_root(root)

main()

