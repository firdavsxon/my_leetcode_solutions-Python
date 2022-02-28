"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it can trap after raining.



Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_index, left_max = 0, height[0]
        right_index, right_max = len(height) - 1, len(height) - 1
        total_rain_water = 0
        while left_index != right_index:
            if height[left_index] < height[right_index]:
                left_index += 1
                left_max = max(left_max, height[left_index])
                total_rain_water += left_max - height[left_index]
            elif height[left_index] >= height[right_index]:
                right_index -= 1
                right_max = max(height[right_index], right_max)
                total_rain_water += right_max - height[right_index]
        return total_rain_water


test =Solution()
height = [4,2,0,3,2,5]
print(test.trap(height))