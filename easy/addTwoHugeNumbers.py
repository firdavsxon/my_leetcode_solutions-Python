"""
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer a

The first number, without its leading zeros.

Guaranteed constraints:
0 ≤ a size ≤ 104,
0 ≤ element value ≤ 9999.

[input] linkedlist.integer b

The second number, without its leading zeros.

Guaranteed constraints:
0 ≤ b size ≤ 104,
0 ≤ element value ≤ 9999.

[output] linkedlist.integer

The result of adding a and b together, returned without leading zeros in the same format.

"""


# Singly-linked lists are already defined with this interface:
class ListNode(object):
	def __init__(self, x):
		self.value = x
		self.next = None


def addTwoHugeNumbers(a:ListNode, b:ListNode) -> ListNode:
	total_sum = get_total_num(a) + get_total_num(b)
	return make_linked_list(total_sum)


def get_total_num(linked_list: ListNode):
	current = linked_list
	temp_num = current.value
	current = current.next
	while current:
		val = current.value
		temp_num = (temp_num *10000) + val
		current = current.next
	return temp_num


def make_linked_list(number: int):
	if not number:
		return None

	temp_list = []
	while number:
		temp_list.append(number % 10000)
		number //= 10000
	output = ListNode(temp_list.pop())
	current = output

	while temp_list:
		while current.next:
			current = current.next
		current.next = ListNode(temp_list.pop())

	return output


def printing_linked_list(linked_list):
	current = linked_list
	while current:
		print(current.value, end=" -> ")
		current = current.next

a = ListNode(0)
# a.next= ListNode(4)
# a.next.next = ListNode(5)

b = ListNode(1234)
b.next = ListNode(123)
b.next.next = ListNode(0)

ll = addTwoHugeNumbers(a, b)
printing_linked_list(ll)
