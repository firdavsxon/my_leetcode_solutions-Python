"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Follow up:

Could you solve this problem without using the library's sort function?
Could you come up with a one-pass algorithm using only O(1) constant space?


Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]

"""
from typing import List
def sortColors(nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for i in range(len(nums)):
            if nums[i] < 1:
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
        right = len(nums)-1
        for j in reversed(range(len(nums))):
            if nums[j] > 1:
                nums[j], nums[right]  = nums[right], nums[j]
                right -= 1

nums = [2,0,2,1,1,0]

sortColors(nums)
print(nums)