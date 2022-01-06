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

	def binary_search(self,arr,lo, hi, key):
		if hi>=1:

			mid =(lo + hi)//2

			if arr[mid] == key:
				return mid

			elif arr[mid] > key:
				return self.binary_search(arr, lo, mid - 1, key)
			else:
				return self.binary_search(arr, mid+1, hi, key)
		return -1



	def binary_search1(self, arr, key):
		start , end = 0, len(arr)-1
		is_ascending = arr[start]<arr[end]
		while start <= end:
			mid = start + (end-start)//2
			if arr[mid] == key:
				return mid
			if is_ascending:
				if arr[mid] > key:
					end = mid -1
				else:
					start = mid+1
			else:
				if arr[mid] < key:
					end = mid - 1
				else:
					start = mid + 1
		return -1


test = Solution()
arr = [1,2,3,4,5,]
arr1 = [5,4,3,2,1]
key = 5
# print(test.binary_search(arr, 0, len(arr), key))
print(test.binary_search1(arr1, key))