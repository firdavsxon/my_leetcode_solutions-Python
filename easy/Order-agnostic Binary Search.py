"""
Problem Statement #
Given a sorted array of numbers, find if a given number ‘key’ is present in the array. Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order. You should assume that the array can have duplicates.

Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

Example 1:

Input: [4, 6, 10], key = 10
Output: 2
Example 2:

Input: [1, 2, 3, 4, 5, 6, 7], key = 5
Output: 4
Example 3:

Input: [10, 6, 4], key = 10
Output: 0
Example 4:

Input: [10, 6, 4], key = 4
Output: 2

"""


class Solution:
	def binary_search(self,arr, key):
		if not arr:
			return -1

		if arr[0]>arr[-1]:
			dec = True
		else:
			dec = False
			#    1, 2 ,3 ,4 , 5, 6, 7, 8, 9, 10
		i = 0
		n = len(arr) - 1
		mid = n // 2
		while i < n:
			if arr[mid]==key:
				return mid
			elif arr[mid]>




test = Solution()
arr = [1,2,3,4,6,8,9,10]
key = 10
test.binary_search(arr, key)