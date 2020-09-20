
"""
You are given two non-empty linked lists representing
two non-negative integers. The digits are stored in
reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""
class ListNode(object):
	def init(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution(object):
	def addTwoNumbers(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		dummy = ListNode(0)
		curr = dummy
		carry = 0
		while l1 or l2:
			x = l1.val if l1 else 0
			y = l2.val if l2 else 0

			sum = x + y + carry
			carry = sum // 10

			curr.next = ListNode(sum % 10)
			curr = curr.next

			if l1: l1 = l1.next
			if l2: l2 = l2.next

		if carry: curr.next = ListNode(carry)

		return dummy.next

