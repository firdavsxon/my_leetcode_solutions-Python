"""
Given an array containing 0s, 1s and 2s, sort the array in-place.
You should treat numbers of the array as objects, hence,
we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red,
white and blue; and since our input array also consists of
three different numbers that is why it is called Dutch National Flag problem.

Example 1:

Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]
Example 2:

Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]

"""

def dutch_flag_problem(arr):
	low , high = 0, len(arr) - 1
	for i in range(len(arr)):
		if arr[i] == 0:
			arr[i], arr[low] = arr[low], arr[i]
			low+=1
		elif arr[i] == 1:
			arr[i], arr[high] = arr[high], arr[i]
			high -=1
	return arr

	# low, high = 0, len(arr) -1
	# i=0
	# while i <= high:
	# 	if arr[i] == 0:
	# 		arr[i], arr[low] = arr[low], arr[i]
	# 		i+=1
	# 		low+=1
	# 	elif arr[i] == 1:
	# 		i += 1
	# 	else:
	# 		arr[i], arr[high] = arr[high], arr[i]
	# 		high -=1
	# return arr




nums = [2, 2, 0, 1, 2, 0]
num1 = [1, 0, 2, 1, 0]
print(dutch_flag_problem(num1))


def dutch_national_flag(array):
	low, high = 0, len(array)-1
	i = 0

	while i<=high:
		if array[i] == 0:
			array[i], array[low] = array[low], array[i]
			i+=1
			low+=1
		elif array[i] == 1:
			i+=1
		else:
			array[i], array[high] = array[high], array[i]
			high -=1
	return array


print(dutch_national_flag([2,2,0,1,2,0]))


