"""
Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

Example 1:

Input: [4, 6, 6, 6, 9], key = 6
Output: [1, 3]
Example 2:

Input: [1, 3, 8, 10, 15], key = 10
Output: [3, 3]
Example 3:

Input: [1, 3, 8, 10, 15], key = 12
Output: [-1, -1]

"""

class Solution:

	def find_range(self, arr, key):
		result = [-1, -1]
		start, end = 0, len(arr)-1
		while start<= end:
			mid = start + (end-start)//2
			
			if arr[mid]>key:
				end = mid -1
			elif arr[mid]<key:
				start = mid + 1
			else:
				start =mid
				end = mid
				while start>=0 and arr[start]==key:
					start-=1
				while end<=len(arr)-1 and arr[end]==key:
					end+=1
				return [start+1, end-1]

		return result


test = Solution()

arr = [1,3,8,10,15]
key = 10
print(test.find_range(arr, key))
