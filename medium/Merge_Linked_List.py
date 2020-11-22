"""

Note: Your solution should have O(l1.length + l2.length) time complexity, since this is what you will be asked to accomplish in an interview.

Given two singly linked lists sorted in non-decreasing order, your task is to merge them. In other words, return a singly linked list, also sorted in non-decreasing order, that contains the elements from both original lists.

Example

For l1 = [1, 2, 3] and l2 = [4, 5, 6], the output should be
mergeTwoLinkedLists(l1, l2) = [1, 2, 3, 4, 5, 6];
For l1 = [1, 1, 2, 4] and l2 = [0, 3, 5], the output should be
mergeTwoLinkedLists(l1, l2) = [0, 1, 1, 2, 3, 4, 5].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l1

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] linkedlist.integer l2

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[output] linkedlist.integer

A list that contains elements from both l1 and l2, sorted in non-decreasing order.
"""


class ListNode(object):
	def __init__(self, x):
		self.value = x
		self.next = None


def mergeTwoLinkedLists(l1, l2):
	l3 = ListNode(None)
	min_val = float('-inf')
	current = l3
	while l1 or l2:
		if l1 and l2:
			if l1.value <= l2.value:
				min_val = l1.value
				l1 = l1.next
			elif l1.value > l2.value:
				min_val = l2.value
				l2 = l2.next

			while current.next:
				current = current.next
			current.next = ListNode(min_val)

		if l1 is None:
			while current.next:
				current = current.next
			current.next = l2
			break
		elif l2 is None:
			while current.next:
				current = current.next
			current.next = l1
			break

	return l3.next


def printing(l3):
	if not l3:
		print('Not linked list')
	while l3:
		print(l3.value, end =' ->')
		l3 = l3.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

l2 = ListNode(4)
l2.next = ListNode(5)
l2.next.next = ListNode(6)

l3 = mergeTwoLinkedLists(l1,l2)
printing(l3)