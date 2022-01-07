"""

Rotation Count (medium) #
Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.

You can assume that the array does not have any duplicates.

Example 1:

Input: [10, 15, 1, 3, 8]
Output: 2
Explanation: The array has been rotated 2 times.
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

Input: [4, 5, 7, 9, 10, -1, 2]
Output: 5
Explanation: The array has been rotated 5 times.
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
 Array after 5 rotations:
Example 3:

Input: [1, 3, 8, 10]
Output: 0
Explanation: The array has been not been rotated.
"""


def rotation_count(arr):
	start, end = 0, len(arr) - 1
	if arr[start] < arr[end]:
		return 0
	max_index = find_max(arr, start, end)
	return max_index + 1


def find_max(arr, start, end):
	while start < end:
		mid = start + (end - start) // 2
		if arr[start] < arr[mid]:
			start = mid
		else:
			end = mid
	return start


def rotation_count1(arr):
	start, end = 0, len(arr) - 1
	while start < end:
		mid = start + (end - start) // 2

		if mid < end and arr[mid] > arr[mid + 1]:
			return mid + 1

		if mid > start and arr[mid - 1] > arr[mid]:
			return mid

		if arr[start] < arr[mid]:
			start = mid + 1
		else:
			end = mid - 1
	return 0


arr = [3,3,7,3]
print(rotation_count(arr))
