"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.



Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Each value on each linked list is in the range [1, 10^9].
Your code should preferably run in O(n) time and use only O(1) memory.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
		if headA is None or headB is None:
			return None
		node1, node2 = headA, headB

		while node1 != node2:
			node1 = headB if node1 is None else node1.next
			node2 = headA if node2 is None else node2.next
		return node1

	def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
		if headA is None or headB is None:
			return None
		node1, node2 = headA, headB
		nodes = set()
		while node1:
			if node1 in nodes:
				return node1
			else:
				nodes.add(node1)
		while node2:
			if node2 in nodes:
				return node2
			else:
				nodes.add(node2)

		return None

	def p(self, root):
		cur = root
		while cur:
			print(cur.val, end="->")
			cur = cur.next


def main():
	root1 = ListNode(4)
	root1.next = ListNode(1)
	root1.next.next = ListNode(8)
	root1.next.next.next = ListNode(4)
	root1.next.next.next.next = ListNode(5)
	# root1.next.next.next.next.next = ListNode(6)
	# root1.next.next.next.next.next.next = ListNode(7)
	# root1.next.next.next.next.next.next.next = ListNode(8)

	root2 = ListNode(5)
	root2.next = ListNode(6)
	root2.next.next = ListNode(1)
	root2.next.next.next = ListNode(8)
	root2.next.next.next.next = ListNode(4)
	root2.next.next.next.next.next = ListNode(5)
	# root2.next.next.next.next.next.next = ListNode(7)
	# root2.next.next.next.next.next.next.next = ListNode(8)
	test = Solution()

	print(test.getIntersectionNode(root1, root2))


main()
