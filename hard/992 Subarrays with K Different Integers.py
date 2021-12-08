"""

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

"""
from typing import List
from collections import OrderedDict

class Solution:
	def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
		def helper(nums, k):
			left ,out = 0, 0
			h_map = {}
			for idx, number in enumerate(nums):
				h_map[number]  = h_map.get(number, 0) + 1
				while len(h_map) > k:
					h_map[nums[left]] = h_map.get(nums[left], 0)
					h_map[nums[left]] -= 1
					if h_map[nums[left]] == 0:
						del h_map[nums[left]]
					left += 1
				out += idx - left + 1
			return out
		return helper(nums, k) - helper(nums, k-1)



test = Solution()

nums = [1,2,1,2,3]
k = 2
print(test.subarraysWithKDistinct(nums, k))




				





