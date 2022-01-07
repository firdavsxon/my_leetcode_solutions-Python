"""
Search in Rotated Array (medium) #
Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.

Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8], key = 15
Output: 1
Explanation: '15' is present in the array at index '1'.
  1
  3
  8
  10
  15
 Original array:
 Array after 2 rotations:
  10
  15
  1
  3
  8
Example 2:

Input: [4, 5, 7, 9, 10, -1, 2], key = 10
Output: 4
Explanation: '10' is present in the array at index '4'.
 Original array:
  -1
  2
  4
  5
  7
  9
  10
  4
  5
  7
  9
  10
  -1
  2

"""


def search_rotated_array(arr, key):

	max_index = find_max(arr)
	key_index = binary_search(arr, key, 0, max_index)
	if key_index != -1:
		return key_index
	return binary_search(arr, key, max_index + 1, len(arr) - 1)


def find_max(arr):
	start, end = 0, len(arr) - 1
	while start < end:
		mid = start + (end - start) // 2
		if arr[mid] > arr[mid+1]:
			end = mid
		elif arr[mid]<arr[mid+1]:
			start = mid+1
	return start


def binary_search(arr, key, start, end):
	while start <= end:
		mid = start + (end - start) // 2

		if arr[mid] == key:
			return mid
		elif arr[mid] > key:
			end = mid - 1
		else:
			start = mid + 1
	return -1


def b_s(lst, target):
	start, end = 0, len(lst) - 1
	while start <= end:
		mid = start + (end-start)//2

		if lst[mid] == target:
			return mid

		if lst[start] <= lst[mid]:
			if lst[start] <= target < lst[mid]:
				end = mid - 1
			else:
				start = mid + 1
		else:
			if lst[mid] < target <= lst[end]:
				start = mid + 1
			else:
				end = mid - 1
	return -1


lst = [2, 3,4,5,6,7,0,1]
target = 0
print(b_s(lst, target))