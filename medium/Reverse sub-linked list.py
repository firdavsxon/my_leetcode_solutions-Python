"""

Problem Statement #
Given the head of a LinkedList and two positions ‘p’ and ‘q’,
reverse the LinkedList from position ‘p’ to ‘q’.

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

def reverse_sub(head, p, q):
	pass

def main():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)

	print("Nodes before reversing sub list: ", end='-> ')
	head.print_list()
	result = reverse_sub(head, 2, 4)

	print("Nodes after linnked list sub list reversed: ", end= '-> ')
	# result.print_list()

main()


