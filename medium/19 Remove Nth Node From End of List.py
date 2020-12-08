"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
"""


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) :
		current = head
		d = {}
		i = 0
		while current:
			d[i] = current
			current = current.next
			i += 1

		if len(d) == 1:
			head = None
			return head
		if len(d) <= n:
			return d[1]
		index = len(d) - n
		if index > 0:
			d[index - 1].next = d[index].next
		elif index == len(d) - 1:
			d[len(d)].next = None
		return d[0]

	#otehrs
	def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
		temp = temp2 = head

		for i in range(n):
			temp = temp.next

		if not temp:  # cases like [1] 2
			return head.next

		while temp.next:
			temp = temp.next
			temp2 = temp2.next

		temp2.next = temp2.next.next

		return head

	def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
		count = 0
		current = head
		while current:
			count += 1
			current = current.next

		prev = None
		current = head
		k = count - n
		while k != 0:
			prev = current
			current = current.next
			k -= 1

		if prev is None:
			return head.next
		else:
			prev.next = current.next
			current.next = None
		return head
