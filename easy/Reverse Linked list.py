"""
Problem Statement #
Given the head of a Singly LinkedList, reverse the LinkedList.
Write a function to return the new head of the reversed LinkedList.


"""

class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def print_list(self):
		temp = self
		while temp:
			print(temp.value, end='-> ')
			temp = temp.next
		print()


def reverse(head):
	prev = None
	while head:
		temp = head.next
		head.next = prev
		prev = head
		head = temp
	return prev

def main():
	head = Node(2)
	head.next = Node(4)
	head.next.next = Node(6)
	head.next.next.next = Node(8)
	head.next.next.next.next = Node(10)

	print("Nodes of original linked list are: ", end='-> ')
	head.print_list()
	result = reverse(head)
	print("Nodes of reversed linked list are: ", end='-> ')
	result.print_list()

main()



