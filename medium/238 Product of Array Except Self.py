"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to
the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements
of any prefix or suffix of the array (including the whole array)
fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the
 purpose of space complexity analysis.)

"""
from typing import List

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		length = len(nums)  # length array
		L, R, answer = [0] * length, [0] * length, [0] * length

		L[0] = 1
		for i in range(1, length):
			L[i] = nums[i - 1] * L[i - 1]
		R[length - 1] = 1
		for i in reversed(range(length - 1)):
			R[i] = nums[i + 1] * R[i + 1]
		for i in range(length):
			answer[i] = L[i] * R[i]
		return answer


test = Solution()
print(test.productExceptSelf([1,2,3,4]))



