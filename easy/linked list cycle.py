"""
Given the head of a Singly LinkedList,
write a function to determine if the LinkedList has a cycle in it or not.
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

def main():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)
	head.next.next.next.next.next = Node(6)
	print("Linked list has a cycle: " + str(has_cycle(head)))

	head.next.next.next.next.next.next = head.next.next
	print("Linked list has cycle: " + str(has_cycle(head)))

	head.next.next.next.next.next.next = head.next.next.next
	print("Linked list has a cycle: " + str(has_cycle(head)))
#
# main()


""" 
Similar Problems #
Problem 1: Given the head of a LinkedList with a cycle, 
find the length of the cycle.

Solution: We can use the above solution to find the cycle in the LinkedList. 
Once the fast and slow pointers meet, we can save the slow 
pointer and iterate the whole cycle with another pointer until 
we see the slow pointer again to find the length of the cycle.


"""


def find_cycle_length(head):
	slow, fast = head, head

	while fast is not None and fast.next is not None:
		fast = fast.next.next
		slow = slow.next
		if slow == fast:
			return calculate_cycle_length(slow)
	return 0

def find_cycle_start(head):
	cycle_length = 0
	slow, fast = head, head
	while fast and fast.next:
		fast = fast.next.next
		slow = slow.next
		if slow == fast:
			cycle_length = calculate_cycle_length(slow)
			break
	return find_start(head, cycle_length)


def calculate_cycle_length(slow):
	current = slow
	cycle_length = 0
	while True:
		current = current.next
		cycle_length += 1
		if current == slow:
			break
	return cycle_length


def find_start(head, cycle_length):
	pointer1, pointer2 = head, head
	while cycle_length > 0:
		pointer2 = pointer2.next
		cycle_length -= 1
	while pointer1 != pointer2:
		pointer1 = pointer1.next
		pointer2 = pointer2.next
	return pointer1


def main2():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)
	head.next.next.next.next.next = Node(6)
	head.next.next.next.next.next.next = head.next.next
	print("Linked list cycle start: " + str(find_cycle_start(head).value))

	head.next.next.next.next.next.next = head.next.next.next
	print("Linked list cycle start: " + str(find_cycle_start(head).value))

	head.next.next.next.next.next.next = head
	print("Linked list cycle start: " + str(find_cycle_start(head).value))


main2()