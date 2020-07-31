"""
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]


Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.

"""

from typing import List, Set


class Solution:
	def intersection(self, nums1: List[int], nums2: List[int]) -> Set[int]:
		s1 = set(nums1)
		s2 = set(nums2)
		return s1.intersection(s2)


test = Solution()
print(test.intersection([1, 2, 2, 1], [2, 2]))
