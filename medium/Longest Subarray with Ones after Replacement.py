"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

Example 1:

Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
Example 2:

Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""
from typing import List


class Solution:
	def length_of_longest_substring(self, lst: List[int], k: int) -> int:
		window_start, max_length, max_ones_count = 0, 0, 0

		for window_end in range(len(lst)):
			if lst[window_end] == 1:
				max_ones_count += 1
			if (window_end - window_start+1 - max_ones_count) > k:
				if lst[window_start] == 1:
					max_ones_count -= 1
				window_start += 1
			max_length = max(max_length, window_end-window_start+1)
		return max_length


test = Solution()
print(test.length_of_longest_substring(lst=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2))
print(test.length_of_longest_substring(lst=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3))

