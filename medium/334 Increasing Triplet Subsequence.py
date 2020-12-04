"""
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
"""
from typing import List


class Solution:
	def increasingTriplet(self, nums: List[int]) -> bool:
		if len(nums)<3:
			return False

		middle  = max(nums)
		min_num = max(nums)

		for i in range(len(nums)):
			if min_num<middle<nums[i]:
				return True
			elif nums[i]<=min_num:
				min_num = nums[i]
			elif min_num <nums[i]<=middle:
				middle = nums[i]
		return False



test = Solution()
# print(test.increasingTriplet([1,2,3,4,5,6]))
nums = [2,4,-2,-3]
num1= [2147483646,2147483647,2147483647]
print(test.increasingTriplet(nums))