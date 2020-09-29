"""
Cyclic Sort (easy)
We'll cover the following
Problem Statement
Try it yourself
Solution
Code
Time complexity
Space complexity
Problem Statement #
We are given an array containing ‘n’ objects. Each object,
when created, was assigned a unique number from 1 to ‘n’ based
 on their creation sequence. This means that the object with
 sequence number ‘3’ was created just before the object with
 sequence number ‘4’.

Write a function to sort the objects in-place on their creation
 sequence number in O(n)O(n) and without any extra space.
 For simplicity, let’s assume we are passed an integer array
 containing only the sequence numbers, though each number is
 actually an object.

Example 1:

Input: [3, 1, 5, 4, 2]
Output: [1, 2, 3, 4, 5]
Example 2:

Input: [2, 6, 4, 3, 1, 5]
Output: [1, 2, 3, 4, 5, 6]
Example 3:

Input: [1, 5, 6, 4, 3, 2]
Output: [1, 2, 3, 4, 5, 6]

"""


def cyclyc_sort(lst):
	i = 0
	while i < len(lst):
		j = lst[i]
		if j != i + 1:
			lst[i], lst[j - 1] = lst[j - 1], lst[i]
		else:
			i += 1
	return lst


def find_missing_number(lst):
	i = 0
	while i < len(lst):
		j = lst[i]
		if lst[i] < len(lst) and lst[i] != j:
			lst[i], lst[j] = lst[j], lst[i]
		else:
			i += 1
	for i in range(len(lst)):
		if lst[i]!=i:
			return i
	return lst

def find_missing_numbers(lst):
	x=[]
	i = 0
	while i < len(lst):
		j = lst[i]-1
		if lst[i] != lst[j]:
			lst[i], lst[j] = lst[j], lst[i]
		else:
			i+=1

	for i, num in enumerate(lst,1):
		if num!=i:
			x.append(i)
	return x


"""
Problem Statement #
We are given an unsorted array containing ‘n+1’ numbers 
taken from the range 1 to ‘n’. The array has only one duplicate 
but it can be repeated multiple times. Find that duplicate number 
without using any extra space. You are, however, allowed to 
modify the input array.

Example 1:

Input: [1, 4, 4, 3, 2]
Output: 4
Example 2:

Input: [2, 1, 3, 3, 5, 4] 
Output: 3
"""

def find_duplicate(lst):
	i = 0
	while i < len(lst):
		j = lst[i]
		if lst[i]!=lst[j-1]:
			lst[i], lst[j-1] = lst[j-1], lst[i]
		elif lst[i] < i+1:
			return lst[i]
		else:
			i+=1
	return None

def find_duplicate1(lst):
	slow, fast = lst[0], lst[lst[0]]
	while slow != fast:
		slow = lst[slow]
		fast = lst[lst[fast]]

	current = lst[lst[slow]]
	cycle_length = 1
	while current !=lst[slow]:
		current = lst[current]
		cycle_length += 1
	return find_start(lst, cycle_length)

def find_start(lst, cycle_length):
	pointer1, pointer2 = lst[0], lst[0]
	while cycle_length > 0:
		pointer2 = lst[pointer2]
		cycle_length -= 1

	while pointer1 != pointer2:
		pointer1 = lst[pointer1]
		pointer2 = lst[pointer2]

	return pointer1

""" 
Find the Corrupt Pair (easy) #
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array originally contained all the numbers from 1 to ‘n’, but due to a data error,
 one of the numbers got duplicated which also resulted in one number going missing. 
 Find both these numbers.
 Example 1:

Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
Example 2:

Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
"""

def find_corrupt_numbers(lst):
	i = 0
	while i < len(lst):
		j = lst[i] - 1
		if lst[i] != lst[j]:
			lst[i], lst[j] = lst[j], lst[i]
		else:
			i += 1
	output = []
	for i, num in enumerate(lst,1):
		if num < i:
			output.append(num)
			output.append(i)
	return output

""" 
Find the Smallest Missing Positive Number (medium) #
Given an unsorted array containing numbers, find the smallest missing positive number in it.

Example 1:

Input: [-3, 1, 5, 4, 2]
Output: 3
Explanation: The smallest missing positive number is '3'
Example 2:

Input: [3, -2, 0, 1, 2]
Output: 4
Example 3:

Input: [3, 2, 5, 1]
Output: 4
"""

def find_missing_positive(lst):
	i = 0
	while i < len(lst):
		j = lst[i] - 1
		if 0 < lst[i] <= len(lst) and lst[i] != lst[j]:
			lst[i], lst[j] = lst[j], lst[i]
		else:
			i += 1

	for i, num in enumerate(lst, 1):
		if num != i:
			return i
	return 0

# [-2, 1, 0 , 3, 2]
print(find_missing_positive([-2, 1, 0 , 3, 2]))
