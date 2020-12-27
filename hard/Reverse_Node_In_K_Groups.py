"""
Note: Your solution should have O(n) time complexity, where n is the number of elements in l, and O(1) additional space complexity, since this is what you would be asked to accomplish in an interview.

Given a linked list l, reverse its nodes k at a time and return the modified list. k is a positive integer that is less than or equal to the length of l. If the number of nodes in the linked list is not a multiple of k, then the nodes that are left out at the end should remain as-is.

You may not alter the values in the nodes - only the nodes themselves can be changed.

Example

For l = [1, 2, 3, 4, 5] and k = 2, the output should be
reverseNodesInKGroups(l, k) = [2, 1, 4, 3, 5];
For l = [1, 2, 3, 4, 5] and k = 1, the output should be
reverseNodesInKGroups(l, k) = [1, 2, 3, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] and k = 3, the output should be
reverseNodesInKGroups(l, k) = [3, 2, 1, 6, 5, 4, 9, 8, 7, 10, 11].
Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
1 ≤ list size ≤ 104,
-109 ≤ element value ≤ 109.

[input] integer k

The size of the groups of nodes that need to be reversed.

Guaranteed constraints:
1 ≤ k ≤ l size.

[output] linkedlist.integer

The initial list, with reversed groups of k elements.
"""


# Singly-linked lists are already defined with this interface:
class ListNode(object):
	def __init__(self, x):
		self.value = x
		self.next = None


def reverseNodesInKGroups(l, k):
	if k == 0:
		return l
	p = l
	counter = 0
	while p:
		counter += 1
		p=p.next
	for i in range(0, counter, k):
		if i+k>counter:
			break
		l = reverse_sub(l, i+1, i + k)
	return l


def reverse_sub(node, p1, p2):
	if p1 == p2:
		return node
	i, prev, current = 0, None, node
	while current and i < p1 - 1:
		prev = current
		current = current.next
		i += 1
	last_node_pf_first_part = prev
	last_node_of_sub_list = current
	i = 0
	while current and i < p2 - p1 + 1:
		temp_next = current.next
		current.next = prev
		prev = current
		current = temp_next
		i += 1

	if last_node_pf_first_part:
		last_node_pf_first_part.next = prev
	else:
		node = prev

	last_node_of_sub_list.next = current
	return node

def printing(l):
	while l:
		print(l.value, end=' -> ')
		l = l.next


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
l.next.next.next.next.next = ListNode(6)
l.next.next.next.next.next.next = ListNode(7)
l.next.next.next.next.next.next.next = ListNode(8)
l.next.next.next.next.next.next.next.next = ListNode(9)
l.next.next.next.next.next.next.next.next.next= ListNode(10)
l.next.next.next.next.next.next.next.next.next.next= ListNode(11)



l = reverseNodesInKGroups(l, 3)
printing(l)
# lr = reverse_sub(l, 4, 6)
# printing(lr)
