class Comaparasion:

	def __init__(self, val):
		self.val = val

	def compare(self, input_val, condition):
		if condition == ">":
			return self.val > input_val
		elif condition == "<":
			return self.val < input_val
		else:
			return self.val == input_val


class ComplexComparation(Comaparasion):

	def complex_com(self, inputs):
		for item in inputs:
			result = self.compare(item[0], item[1])
			if result:
				print(f"{str(item[0])} >= {self.val} ")

			else:
				print(f"{str(item[0])} < {self.val} ")


test = Comaparasion(5)
# print(test.compare(1))
test1 = ComplexComparation(5)
# test1.complex_com([1, 3, 4, 6, 7, 0])


# 5 > 1 True

# 5>1 and 5>10


def printing_linked_list(linked_list):
	current = linked_list
	while current:
		print(current.val, end =' -> ')
		current = current.next


class LinkedList:
	def __init__(self, val):
		self.val = val
		self.next = None
		self.prev = None


head = LinkedList(6)
head.next = LinkedList(5)
head.next.next = LinkedList(4)
head.next.next.next = LinkedList(3)
head.next.next.next.next = LinkedList(2)
# printing_linked_list(head)



class Queue:

	def __init__(self, queue_limit):
		self.queue_limit = queue_limit
		self.queue = ['']*self.queue_limit
	def get(self):
		if len(self.queue)==0:
			return "queueu is empty"
		else:
			return self.queue[0]

	def pop(self):
		if self.queue[0] != '':
			popped_item = self.queue[0]
			for idx, item in enumerate(self.queue):
				if idx>0:
					self.queue[idx-1] = item
			return popped_item
		return 'queue is empty'


	def push(self, input_value):
		print(self.queue)
		if self.queue[-1]=='':
			for idx, string in enumerate(self.queue):
				if string == "":
					self.queue[idx] = input_value
					print(self.queue)
					return
		return 'queueu is full'


queue = Queue(2)

print(queue.push(2))
print(queue.push(5))
print(queue.pop())
print(queue.push(5))


