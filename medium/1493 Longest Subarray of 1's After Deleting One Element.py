"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4
Example 5:

Input: nums = [0,0,0]
Output: 0

"""
from typing import List

class Solution:
	def longestSubarray(self, nums: List[int]) -> int:
		start, max_length, max_zero_count = 0,0,0

		for right, num in enumerate(nums):
			if num == 0:
				max_zero_count += 1

			while max_zero_count > 1:
				if nums[start] == 0:
					max_zero_count -= 1
				start += 1

			max_length = max(max_length, right - start )
		return max_length


test = Solution()
nums = [1,1,0,1]
print(test.longestSubarray(nums))
