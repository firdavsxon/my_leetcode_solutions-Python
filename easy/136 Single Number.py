"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

"""
from typing import List


class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		# using extra memoery
		d = {}
		for i in nums:
			if i not in d: d[i] = 1
			elif i in d: d[i] = 2
		for key, val in d.items():
			if val == 1: return key

	def singleNumber1(self, nums: List[int])->int:
		# not using memory
		nums.sort()
		i = 1
		while i < len(nums):
			if nums[i-1] != nums[i]:
				return nums[i-1]
			i += 2
		return nums[-1]
# soluton from others
	def singleNumber2(self, nums:List[int])->int:
		#in place
		i = 0
		while i < len(nums):
			if nums[i] not in nums[:i] + nums[i+1:]:
				return nums[i]
			i += 1
		return 0
#solution from others
	def singleNumber3(self, nums: List[int]) -> int:
		return 2 * (sum(set(nums))) - sum(nums)

	def singleNumber4(self, nums: List[int])->int:
		a=0
		for i in nums:
			a ^=i
		return a






test = Solution()
# print(test.singleNumber([2,2,1]))
# print(test.singleNumber([4,1,2,1,2]))
print(test.singleNumber1([2,3,2,1,3,4,4,41,41,1,52]))
print(test.singleNumber4([2,2,1]))
print(test.singleNumber4([4,1,2,3,3,1,2]))
print(test.singleNumber4([1,1,2,2,3,3,4,5,5,6,6])) # [2,]
