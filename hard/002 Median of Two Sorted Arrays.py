"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run
time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = nums1+nums2
        x.sort()
        if len(x) % 2 != 0:
            return x[len(x)//2]
        midx = len(x)//2
        return (x[midx] + x[midx-1]) / 2


test = Solution()
print(test.findMedianSortedArrays([1, 2], [3, 4]))