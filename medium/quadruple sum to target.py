"""
Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

Example 1:

Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
Example 2:

Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.


"""

def search_quadruplets(arr, target):
	quadruplets = []
	arr.sort()
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			left = j+1
			right = len(arr)-1

			while left < right:
				summa = arr[i] + arr[j] + arr[left] + arr[right]

				if summa > target:
					right -=1
				elif summa < target:
					left += 1
				else:
					quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
					left +=1
					right -=1

	return quadruplets

nums= [2, 0, -1, 1, -2, 2]
nums2 = [4, 1, 2, -1, 1, -3]
nums1 = [2,2,2,2,2]

print(search_quadruplets(nums1, 8))

# [4, 1, 2, -1, 1, -3]
# [-3, -1, 1, 1, 2, 4]
def search_quadreplets(arr, target):
	arr.sort()
	for i in range(len(arr)):
		current = arr[i]
