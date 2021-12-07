"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
Example 3:

Input: nums = [1,-1], k = 1
Output: [1,-1]
Example 4:

Input: nums = [9,11], k = 2
Output: [11]
Example 5:

Input: nums = [4,-2], k = 2
Output: [4]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

"""
from typing import List

class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		from collections import deque
		queue = deque()
		res = []
		left = right = 0
		size = len(nums)
		while right < size:
			while queue and (nums[right] > nums[queue[-1]]):
				queue.pop()
			queue.append(right)

			if left > queue[0]:
				queue.popleft()
			if right + 1 >= k:
				res.append(nums[queue[0]])
				left += 1
			right += 1
		return res
	
	def max_sliding_window(self, nums, k):
		max_num, window_start = float('-inf'), 0
		res = []
		for window_end in range(len(nums) + 1):

			if window_end - window_start == k:
				current_max = max(nums[window_start:window_end ])
				max_num = max(max_num, current_max)
				res.append(current_max)
				window_start += 1

		return res
		
		

test = Solution()
nums1 =[1,3,-1,-3,5,3,6,7]
nums= [1,-1]
k = 1
print(test.maxSlidingWindow(nums, k))
print(test.max_sliding_window(nums,k))