"""

Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; after removing the
duplicates in-place return the new length of the array.

Example 1:

Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
Example 2:

Input: [2, 2, 2, 11]
Output: 2
Explanation: The first two elements after removing the duplicates will be [2, 11].

"""
from typing import List


class Solution:

	def remove_duplicates(self, array: List[int]) -> int:
		if len(array)<2:
			return len(array)

		non_duplicate = 0

		for index in range(1, len(array)):
			if array[index] != array[index-1]:
				non_duplicate += 1
		return non_duplicate + 1

	def remove_duplicatesII(self, array: List[int], key: int) -> int:
		non_duplicate = len(array)
		for num in array:
			if num!=key:
				non_duplicate -= 1
		return len(array) - non_duplicate





test = Solution()
array1 = [1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9]
array2 = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5,5,6,6,6]
array = [1,1,1,2]
print(test.remove_duplicatesII(array, 1))



""" 
Similar Questions #
Problem 1: Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

Example 1:

Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
Example 2:

Input: [2, 11, 2, 2, 1], Key=2
Output: 2
Explanation: The first two elements after removing every 'Key' will be [11, 1].
"""



