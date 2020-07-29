"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

"""
from typing import List, Union


class Solution:
	def searchInsert(self, nums: List[int], target: int) -> Union[int, str]:
		if target in nums:
			return f'Target {target} in list {nums} and position is : {nums.index(target)}'
		nums.append(target)
		nums.sort()
		return f'Target {target} in list {nums} and position in list index should be : {nums.index(target)}'

	def searchInsert1(self, nums, target):
		for i in range(0, len(nums)):
			num = nums[i]
			if num >= target:
				return i

		return len(nums)


test = Solution()
test1 = test.searchInsert([1,2,3,4,7,9], 0)
print(test1)
