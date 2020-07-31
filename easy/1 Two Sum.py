"""
Given an array of integers, return indices of the
two numbers such that they add up to a specific target.

You may assume that each input would have exactly one
solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
from typing import List

class Solution:
	def twoSum1(self, nums: List[int], target: int) -> List[int]:
		# brute force
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if nums[j] + nums[i] == target:
					return [i, j]

	def twoSum(selfself, nums: List[int], target: int) -> List[int]:
		d = {}

		for i in range(len(nums)):
			if target - nums[i] not in d:
				d[nums[i]] = i
			else:
				return [d[target - nums[i]], i]

test = Solution()
print(test.twoSum(nums = [2, 7, 11, 15], target = 9))
print(test.twoSum(nums = [2,5,5,11], target = 10))
