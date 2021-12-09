"""
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example 1:

Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
Example 2:

Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
Example 3:

Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted
Example 4:

Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
"""

def shortest_window_sort(arr):
	low, high = 0, len(arr)-1
	while low <= len(arr)-1 and arr[low]<=arr[low+1]:
		low+=1

	if low == len(arr)-1: # if array sorted
		return 0

	while high > 0 and arr[high] >= arr[high-1]:
		high -= 1

	subarray_max = -float('inf')
	subarray_min = float('inf')

	for k in range(low, high+1):
		subarray_max = max(subarray_max, arr[k])
		subarray_min = min(subarray_min, arr[k])

	while low >0 and arr[low-1] > subarray_min:
		low -= 1

	while high < len(arr) -1 and arr[high+1] < subarray_max:
		high +=1

	return high-low+1



def new_functions_for_test_knodledge(nums):
	low, high = 0, len(nums)-1
	while low<len(nums)-1 and nums[low]<=nums[low+1]:
		low+=1

	if low == len(nums) - 1:
		return 0

	while high > 0 and nums[high] >= nums[high-1]:
		high -=1

	subarray_max_number = float('-inf')
	subarray_min_number = float('inf')

	for k in range(low, high+1):
		subarray_max_number = max(subarray_max_number, nums[k])
		subarray_min_number = min(subarray_min_number, nums[k])
		
	
	while low>0  and nums[low-1]> nums[low]:
		low-=1
	
	while high<len(nums)-1 and nums[high]> nums[high+1]:
		high+=1
	
	return high-low+1

	


nums = [3, 2, 1]
nums1 = [1, 2, 5, 3, 7, 10, 9, 12]
print(shortest_window_sort(nums1))
print(new_functions_for_test_knodledge(nums1))