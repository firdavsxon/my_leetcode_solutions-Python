"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.



The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.



Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""
from typing import List


class Solution:
	def maxArea(self, height: List[int]) -> int:
		max_container, start = 0, 0
		end = len(height)-1

		while start < end:
			max_container = max(max_container, ((end-start)*min(height[start], height[end])))

			if height[end] >= height[start]:
				start += 1
			elif height[end] < height[start]:
				end -= 1
		return max_container


test = Solution()
print(test.maxArea([1, 2, 1]))

