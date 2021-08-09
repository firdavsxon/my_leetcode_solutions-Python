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
		# s1 = set(nums1)
		# s2 = set(nums2)
		# return s1.intersection(s2)
		res = set()  # only select unique elements
		for i in nums2:  # iterating elements of nums2
			if i in nums1:  # checking weather element[i] present in nums1
				res.add(i)  # adding the intersecting element in res
		return res


test = Solution()
print(test.intersection(nums1 = [2,3,4,8,6],nums2 = [2,6,4,8,9,5]))
