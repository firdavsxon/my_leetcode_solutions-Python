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
	if p ==q:
		return head
	# after skipping 'p-1' nodes, current will point to 'p'th node
	i, prev, current = 0, None, head
	while current and i < p-1:
		prev = current
		current = current.next
		i+=1
	# we are interested in three part of the linked list, the part before index 'p',
	# the part between 'p' and 'q', and the part after index 'q'
	last_node_of_first_part = prev
	# after reversing the linked list 'current' will become the last node of the sub-list
	last_node_of_sub_list = current

	i=0
	# reverse nodes between 'p' and 'q'
	while current and i < q-p+1:
		temp_next = current.next # temp_next will temporarily have next node
		current.next = prev
		prev = current
		current = temp_next
		i += 1

	# connect with the first part
	if last_node_of_first_part:
		# 'prev' is now the first node of the sub-list
		last_node_of_first_part.next = prev
		# this means p = 1 i.e., we are changing the first node (head) of the linked list
	else:
		head = prev
	# connect with the last part
	last_node_of_sub_list.next = current
	return head


def main():
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(3)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(5)

	print("Nodes before reversing sub list: ", end='-> ')
	head.print_list()
	result = reverse_sub(head, 2, 4)

	print("Nodes after linnked list sub list reversed: ", end='-> ')
	result.print_list()

main()


