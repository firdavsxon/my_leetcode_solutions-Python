"""
Top 'K' Numbers (easy)
We'll cover the following
Problem Statement
Try it yourself
Solution
Code
Time complexity
Space complexity
Problem Statement #
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

Example 1:

Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
Example 2:

Input: [5, 12, 11, -1, 12], K = 3
Output: [12, 11, 12]
"""
from heapq import *


class Solution:

	def find_k_largest_numbers(self, nums, k):
		min_heap = []
		for i in range(k):
			heappush(min_heap, nums[i])

		for i in range(k, len(nums)):
			if nums[i] > min_heap[0]:
				heappop(min_heap)
				heappush(min_heap, nums[i])
		return list(min_heap)


test = Solution()
array = [3, 1, 5, 12, 2, 11]
k = 3
print(test.find_k_largest_numbers(array, k))