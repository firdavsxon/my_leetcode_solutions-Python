

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
		dummy = ListNode(-1)
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