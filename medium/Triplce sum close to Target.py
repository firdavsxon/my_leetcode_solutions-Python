"""
Problem Statement #
Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

Example 1:

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
Example 2:

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
Example 3:

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.

"""

def triple_sum_closest_to_target(arr, target):
	arr.sort()
	closest = float('inf')
	for i in range(len(arr)):
		left = i+1
		right = len(arr) - 1
		while left < right:
			summa = arr[i] + arr[left] + arr[right]

			if summa > target:
				closest = min(closest, summa)
				right -= 1
			elif summa < target:
				closest = max(closest, summa)
				left +=1
	return closest

	# for i in range(len(arr)):
	# 	left = i+1
	# 	right = len(arr)-1
	# 	while left < right:
	# 		target_difference = target - arr[i] - arr[left] - arr[right]
	# 		if target_difference == 0:
	# 			return target - target_difference
	# 		if abs(target_difference) < abs(closest):
	# 			closest = target_difference
	# 		if target_difference > 0:
	# 			left +=1
	# 		else:
	# 			right -= 1
	#
	# return target - closest



nums = [-2, 0, 1, 2]
nums2 = [-3, -1, 1, 2]
nums3 = [1, 0, 1, 1]
nums4 = [2, 3, 4, 6]
print(triple_sum_closest_to_target(nums4, 7))