"""
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such
that you cannot load all elements into the memory at once?
"""
from typing import List
from collections import Counter
class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		d ={}
		res=[]
		for i in nums1:
			if i in d:
				d[i] += 1
			else:
				d[i] = 1
		for i in nums2:
			if i in d:
				res.append(i)
				d[i] -= 1

				if d[i]==0:
					d.pop(i)
		return res

	def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
		n1_counter, n2_counter = Counter(nums1), Counter(nums2)
		res = []

		for n1_digit in n1_counter:
			if n1_digit in n2_counter:
				intersecting_times = min(n1_counter[n1_digit], n2_counter[n1_digit])
				res += [n1_digit] * intersecting_times

		return res







test = Solution()
# print(test.intersect(nums1=[4,9,5], nums2=[9,4,9,8,4]))
print(test.intersect(nums1=[1,2,2,1], nums2=[2,2]))
# print(test.intersect(nums1=[1], nums2=[1,2]))
# print(test.intersect(nums2=[2], nums1=[1,2, 2,1]))
# print(test.intersect(nums1=[3,1,2], nums2=[1,1]))
# print(test.intersect([54,93,21,73,84,60,18,62,59,89,83,89,25,39,41,55,78,27,65,82,94,61,12,38,76,5,35,6,51,48,61,0,47,60,84,9,13,28,38,21,55,37,4,67,64,86,45,33,41],
# [17,17,87,98,18,53,2,69,74,73,20,85,59,89,84,91,84,34,44,48,20,42,68,84,8,54,66,62,69,52,67,27,87,49,92,14,92,53,22,90,60,14,8,71,0,61,94,1,22,84,10,55,55,60,98,76,27,35,84,28,4,2,9,44,86,12,17,89,35,68,17,41,21,65,59,86,42,53,0,33,80,20]))
