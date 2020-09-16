"""
Problem Statement #
Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.

"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def has_cycle(head):
	slow, fast = head, head
	while fast is not None and fast.next is not None:
		fast = fast.next.next
		slow = slow.next
		if slow == fast:
			return True
	return False

def find_cycle_length(head):
	slow, fast = head, head

	while fast is not None and fast.next is not None:
		fast = fast.next.next
		slow = slow.next
		if slow == fast:
			return calculate_cycle_length(slow)
	return 0


def calculate_cycle_length(slow):
	current = slow
	cycle_length = 0
	while True:
		current = current.next
		cycle_length += 1
		if current == slow:
			break
	return cycle_length
