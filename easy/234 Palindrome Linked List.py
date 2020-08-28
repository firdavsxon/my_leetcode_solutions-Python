# Palindrome Linked List

"""
Given a singly linked list, determine if it is a palindrome.

Example 1:
Input: 1->2
Output: false

Example 2:
Input: 1->2->2->1
Output: true

Follow up:
Could you do it in O(n) time and O(1) space?

"""


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		l = []
		while head:
			l.append(head.val)
			head = head.next
		return l == l[::-1]

	def isPalindrome1(self, head: ListNode):



		current_node = head

		slow, fast = head, head

		while fast is not None and fast.next is not None:
			slow = slow.next
			fast = fast.next.next

		rev_node = self.reverse(slow)

		while rev_node and current_node:

			if rev_node.val != current_node.val:
				return False

			rev_node = rev_node.next
			current_node = current_node.next

		return True

	def reverse(self, slow):
		prev = None

		while slow:
			temp = slow.next
			slow.next = prev

			prev = slow
			slow = temp

		return prev


test = Solution()
print(test.isPalindrome([1,2]))
