"""

Search Bitonic Array (medium) #
Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

Example 1:

Input: [1, 3, 8, 4, 3], key=4
Output: 3
Example 2:

Input: [3, 8, 3, 1], key=8
Output: 1
Example 3:

Input: [1, 3, 8, 12], key=12
Output: 3
Example 4:

Input: [10, 9, 8], key=10
Output: 0
Solution #
"""

def search_bitonic_array(arr, key):
	max_index = find_max(arr)
	key_index1 = binary_search(arr, key, 0, max_index)
	key_index2 = binary_search(arr, key, max_index+1, len(arr)-1)
	if key_index1!= -1:
		return key_index1
	if key_index2!=-1:
		return key_index2
	return -1

def find_max(arr):
	start, end = 0, len(arr)-1
	while start < end:
		mid = start + (end-start)//2

		if arr[mid] > arr[mid+1]:
			end = mid
		else:
			start = end +1
	return start


def binary_search(arr, key, start, end):
	while start<=end:
		mid = start + (end - start)//2

		if arr[mid] == key:
			return mid
		elif arr[mid] > key:
			end = mid -1
		else:
			start = mid +1
	return -1


arr = [10, 9 ,8 ]
key = 10
print(search_bitonic_array(arr, key))