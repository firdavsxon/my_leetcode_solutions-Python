"""
Problem Statement #
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set.
For example, {1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!n! permutations.
"""
from collections import deque
def find_permutation(nums):
	nums_length = len(nums)
	result = []
	permutations = deque()
	permutations.append([])
	for current_number in nums:
		n = len(permutations)
		for _ in range(n):
			old_permutation = permutations.popleft()
			for j in range(len(old_permutation)+1):
				new_permutation = list(old_permutation)
				new_permutation.insert(j ,current_number)
				if len(new_permutation) == nums_length:
					result.append(new_permutation)
				else:
					permutations.append(new_permutation)
	return result


def find_permutations_recursive(nums):
	result = []
	generate_permuattions_recuresive(nums, 0, [], result)
	return result


def generate_permuattions_recuresive(nums, index, current_permutation, result):
	if index == len(nums):
		result.append(current_permutation)
	else:
		for i in range(len(current_permutation)+1):
			new_permutation = list(current_permutation)
			new_permutation.insert(i, nums[index])
			generate_permuattions_recuresive(nums, index +1, new_permutation, result)


print(find_permutations_recursive([1,3,5]))