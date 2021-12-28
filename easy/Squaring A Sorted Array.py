"""
Problem Statement #
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

Example 1:

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]
Example 2:

Input: [-3, -1, 0, 1, 2]
Output: [0 1 1 4 9]

"""

def make_squares(arr):
	squares = []
	left = 0
	right = len(arr)-1

	while left < right:
		if arr[left]**2 > arr[right]**2:
			squares.append(arr[left]**2)
			squares.append(arr[right] ** 2)
		else:
			squares.append(arr[right]**2)
			squares.append(arr[left]**2)
		left+=1
		right-=1
		if left==right:
			squares.append(arr[right] ** 2)
			break
	return squares[::-1]


def make_square_groock(arr):
	size = len(arr)
	squares = [0 for x in range(size)]
	highest_square_idx = size-1
	left, right =0 ,size -1
	while left < right:
		left_square = arr[left] **2
		right_square = arr[right]**2
		if left_square>right_square:
			squares[highest_square_idx]=  left_square
			left+=1
		else:
			squares[highest_square_idx] = right_square
			right -= 1
		highest_square_idx -= 1
	return squares
nums = [-2, -1, 0, 2, 3]
print(make_squares(nums))
print(make_square_groock(nums))


def make_square(array):
	if len(array) == 0:
		return []
	if len(array) == 1:
		return [array[0]**2]
	new_array = []
	left = 0
	right = len(array) - 1
	while left != right:
		if array[left] **2 > array[right]**2:
			new_array.append(array[left]**2)
			left +=1
		else:
			new_array.append(array[right]**2)
			right -=1
	new_array.append(array[left]**2)
	return new_array[::-1]


print(make_square([-2, -1, 0, 2, 3]))
