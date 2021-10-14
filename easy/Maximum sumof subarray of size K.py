"""
Problem Statement #
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
Example 2:

Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

"""


def max_sum_of_subarray(lst, k):

	if len(lst) <= k:
		return sum(lst)

	max_num = 0
	for idx, num in enumerate(lst):
		start = idx
		end = start+k
		if end <= len(lst):
			temp_sum = sum(lst[start:end])
			max_num = max(temp_sum, max_num)
			end += 1
			start += 1
	return max_num


print(max_sum_of_subarray([2, 1, 5, 1, 3, 2], 3))
print(max_sum_of_subarray([2, 3, 4, 1, 5], 2))