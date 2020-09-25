"""

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one
that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity.
Could you implement it using only constant extra space complexity?
"""
from typing import List

class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		# missing = len(nums)
		# for i, num in enumerate(nums):
		# 	missing ^= i ^ num
		# return missing
		nums.sort()
		if nums[0]!=0:
			return 0
		if nums[-1]!=len(nums):
			return len(nums)
		for i in range(1,len(nums)):
			if nums[i] - nums[i-1]!=1:
				return nums[i-1]+1


test =Solution()
print(test.missingNumber([5,2,3,0,1]))