"""Array Quadruplet

Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).

Explain and code the most efficient solution possible, and analyze its time and space complexities.

Example:

input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)
Constraints:

[time limit] 5000ms

[input] array.integer arr

1 ≤ arr.length ≤ 100
[input] integer s

[output] array.integer
"""


def find_array_quadruplet(arr, s):
	# arr.sort()
	# n=len(arr)
	# if n < 4:
	# 	return []
	#
	# for i in range(n - 4):
	# 	for j in range(i + 1, n - 3):
	#
	# 		k = s - (arr[i] + arr[j])  # k stores ramaning sum
	# 		low = j + 1
	# 		high = n - 1
	#
	# 		while low < high:
	# 			if arr[low] + arr[high] < k:
	# 				low += 1
	# 			elif arr[low] + arr[high] > k:
	# 				high -= 1
	# 			else:
	# 				return [arr[i], arr[j], arr[low], arr[high]]
	# return []
	res = []
	if not arr or len(arr)<4:
		return res
	size = len(arr)
	arr.sort()

	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			left = j+1
			right = size-1
			while left < right:
				summa = arr[i] + arr[j] + arr[left] + arr[right]
				if summa == s:
					temp_list = [arr[i], arr[j], arr[left], arr[right]]
					res.append(temp_list)
					left_value = arr[left]
					while left < size and arr[left] == left_value:
						left += 1
					right_value = arr[right]
					while right > left and arr[right] == right_value:
						right -= 1
				elif summa < s:
					left += 1
				else:
					right -= 1
			while j+1 < size and arr[j + 1] == arr[j]:
				j += 1
		while i+1 < size and arr[i+1] == arr[i]:
			i += 1
	return res


print(find_array_quadruplet(arr=[2, 7, 4, 0, 9, 5, 1, 3], s=20))
print(find_array_quadruplet(arr=[1, 0, -1, 0, -2, 2], s=0))
