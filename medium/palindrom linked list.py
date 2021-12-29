"""
Given the head of a Singly LinkedList, write a method to
check if the LinkedList is a palindrome or not.

Your algorithm should use constant space and the input
LinkedList should be in the original form once the algorithm
is finished. The algorithm should have
O
(
N
)
O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

Example 1:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:

Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false

"""

class Node:
	def __init__(self, value, next = None):
		self.value = value
		self.next = next

def is_palindrome(head):
	slow, fast = head, head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	head_of_second_half = reverse(slow)
	copy_head_of_second_half = head_of_second_half
	while head and head_of_second_half:
		if head.value != head_of_second_half.value:
			break
		head = head.next
		head_of_second_half = head_of_second_half.next
	reverse(copy_head_of_second_half)

	if head is None and head_of_second_half is None:
		return True
	return False


def reverse(head):
	prev = None
	while head:
		temp_next = head.next
		head.next = prev
		prev = head
		head = temp_next
	return prev




def main():
	head = Node(1)
	head.next  = Node(2)
	head.next.next = Node(2)
	head.next.next.next = Node(1)

	print("Linked list is palindrome: " + str(is_palindrome(head)))

	head.next.next.next.next = Node(2)

	print("Linked list is a planidrome: " + str(is_palindrome(head)))

main()

