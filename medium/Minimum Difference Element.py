"""

Problem Statement #
Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.

Example 1:

Input: [4, 6, 10], key = 7
Output: 6
Explanation: The difference between the key '7' and '6' is minimum than any other number in the array
Example 2:

Input: [4, 6, 10], key = 4
Output: 4
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: 10
Example 4:

Input: [4, 6, 10], key = 17
Output: 10
"""


class Solution:

	def search_min_diff_element(self, arr, key):
		if key<arr[0]:
			return arr[0]
		elif key>arr[-1]:
			return arr[-1]

		start, end = 0, len(arr)-1
		difference = float('inf')
		out = -1

		while start <= end:
			mid = start +(end-start)//2
			if arr[mid] == key:
				return arr[mid]
			elif arr[mid] > key:
				diff = abs(key - arr[mid])
				if diff<difference:
					difference = diff
					out = arr[mid]
				end = mid -1
			else:
				diff = abs(key - arr[mid])
				if diff < difference:
					difference = diff
					out = arr[mid]
				start = mid + 1

		return out



test = Solution()
arr = [1 ,3, 8, 10, 15]
key = 17
print(test.search_min_diff_element(arr, key))


""" 

Bitonic Array Maximum (easy)
We'll cover the following
Problem Statement
Try it yourself
Solution
Code
Time complexity
Space complexity
Problem Statement #
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Example 1:

Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.
Example 2:

Input: [3, 8, 3, 1]
Output: 8
Example 3:

Input: [1, 3, 8, 12]
Output: 12
Example 4:

Input: [10, 9, 8]
Output: 10
"""

def find_max_in_biotonic_array(arr):
	start , end = 0, len(arr)-1

	# mid = start + (end-start)//2
	# if arr[start] > arr[mid] and arr[start] > arr[end]:
	# 	return arr[start]
	# elif arr[end]> arr[mid] and arr[end] > arr[start]:
	# 	return arr[end]
	# largest = arr[mid]
	# left = mid-1
	# right = mid +1
	# while largest < arr[left]:
	# 	left -=1
	# while largest < arr[right]:
	# 	right +=1
	#
	# return max(arr[left+1], arr[right-1])
	while start < end:
		mid = start + (end - start)//2
		if arr[mid] > arr[mid+1]:
			end = mid
		else:
			start = mid +1
	return arr[start]


array = [1,2,3,4,5,6,7,8]
print(find_max_in_biotonic_array(array))

