"""
Given a non-empty array of integers, every element appears
three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99

"""
from typing import List
from collections import Counter, defaultdict


class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		# i = 0
		# while i <len(nums):
		#     if nums[i] not in nums[:i] + nums[i+2:]:
		#         return nums[i]
		#     i+=1
		# return 0

		# with extra memory
		# d = {}
		# for num in nums:
		# 	if num not in d:
		# 		d[num] = 1
		# 	elif num in d:
		# 		d[num] = 2
		# for key, val in d.items():
		# 	if val == 1:
		# 		return key
		nums.sort()
		i=0
		while i <len(nums)-1:
			if nums[i]!=nums[i+1] and nums[i]!=nums[i+2]:
				return nums[i]
			i+=3
		return nums[-1]

		# solution from others
	def singleNumber1(self, nums: List[int]) -> int:
		one = 0
		two = 0
		for n in nums:
			one = one ^ n & ~two
			two = two ^ n & ~one
		return one

	def singleNumber2(self, nums: List[int]) -> int:
		hashmap = Counter(nums)

		for k in hashmap.keys():
			if hashmap[k] == 1:
				return k

	def singleNumber3(self, nums: List[int]) -> int:
		hash_table = defaultdict(int)
		for i in nums:
			hash_table[i] += 1

		for i in hash_table:
			if hash_table[i] == 1:
				return i

	def singleNumber4(self, nums: List[int]) -> int:

		return (3 * sum(set(nums)) - sum(nums)) // 2



test = Solution()
print(test.singleNumber([0, 1, 0, 1, 0, 1, 99]))
print(test.singleNumber4([2, 2, 3,1,3,3, 2]))
print(test.singleNumber2([1, 1, 1, 3, 2, 3, 2, 3, 4,2, 5, 5, 5, 6, 7, 6, 7, 6, 7]))
