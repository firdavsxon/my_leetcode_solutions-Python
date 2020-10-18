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
print(test.intersect1(nums1=[4,9,5], nums2=[9,4,9,8,4]))
print(test.intersect1(nums1=[1,2,2,1], nums2=[2,2]))
print(test.intersect1(nums1=[1], nums2=[1,2]))
print(test.intersect1(nums2=[2], nums1=[1,2, 2,1]))
print(test.intersect1(nums1=[3,1,2], nums2=[1,1]))
