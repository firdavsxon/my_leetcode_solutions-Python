"""
Given an integer array nums and an integer k, return true if there are two distinct
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
from typing import List


class Solution:
	def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		d = {}
		for idx, num in enumerate(nums):
			if num not in d:
				d[num] = [idx]
			else:
				d[num].append(idx)
		for key, val in d.items():
			if len(val) > 1:
				for index in val:
					for index2 in val:
						if index!=index2:
							if abs(index - index2) <= k:
								return True
		return False
test = Solution()
nums1 = [0,1,2,3,4,0,0,7,8,9,10,11,12,0]
nums = [1,2,3,1,2,3]
print(test.containsNearbyDuplicate(nums, 2))
