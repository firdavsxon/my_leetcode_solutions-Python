"""
Problem Statement #
Given a set with distinct elements, find all of its distinct subsets.

Example 1:

Input: [1, 3]
Output: [], [1], [3], [1,3]
Example 2:

Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""

def find_subsets(nums):
	list.sort(nums)
	final_subsets = []
	final_subsets.append([])
	start_idx, end_idx= 0, 0
	for i, num in enumerate(nums):
		start_idx = 0
		if i > 0 and nums[i] == nums[i-1]:
			start_idx = end_idx + 1
		end_idx = len(final_subsets) -1
		for j in range(start_idx, end_idx+1):
			new_subset_list_set = list(final_subsets[j])
			new_subset_list_set.append(num)
			final_subsets.append(new_subset_list_set)
	return final_subsets

print(find_subsets([1,5,3]))


def find_sub(nums):
	nums.sort()
	subsets = []
	subsets.append([])
	for num in nums:
		current_level = len(subsets)
		for j in range(current_level):
			new = list(subsets[j])
			new.append(num)
			subsets.append(new)

	return subsets

def find_subs1(nums):
	nums.sort()
	subsets = [[]]
	start_idx, end_idx = 0, 0
	for idx in range(len(nums)):
		start_idx = 0

		if idx > 0 and nums[idx] == nums[idx-1]:
			start_idx = end_idx + 1
		end_idx = len(subsets) -1
		for index in range(start_idx, end_idx+1):
			new = list(subsets[index])
			new.append(nums[idx])
			subsets.append(new)
	return subsets




print(find_subs1([1,2,2]))


