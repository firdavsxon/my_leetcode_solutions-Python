"""
Problem Statement #
Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’
closest numbers to ‘X’ in the array. Return the numbers in the sorted order.
 ‘X’ is not necessarily present in the array.

Example 1:

Input: [5, 6, 7, 8, 9], K = 3, X = 7
Output: [6, 7, 8]
Example 2:

Input: [2, 4, 5, 6, 9], K = 3, X = 6
Output: [4, 5, 6]
Example 3:

Input: [2, 4, 5, 6, 9], K = 3, X = 10
Output: [5, 6, 9]
"""
from heapq import *


def find_closest_elements(arr, K, X):

	result = []
	min_heap=[]
	closest_num = binarch_search(arr, X)

	for idx in range(len(arr)):
		if arr[idx] == closest_num:
			left, right = idx, idx
			heappush(min_heap, arr[idx])
			while len(min_heap)<K:
				left -= 1
				right += 1
				if left>0:
					heappush(min_heap, arr[left])
				if right<len(arr):
					heappush(min_heap, arr[right])
	while min_heap:
		result.append(heappop(min_heap))
	return result



def binarch_search(arr, x):
	if x < arr[0]:
		return arr[0]
	if x > arr[len(arr)-1]:
		return arr[len(arr)-1]
	start, end = 0, len(arr)-1
	while start <= end:
		mid = start + (end-start)//2

		if arr[mid]>x:
			end = mid -1
		elif arr[mid]<x:
			start = mid +1
		else:
			return arr[mid]
	if (arr[start] - x) < (x - arr[end]):
		return arr[start]
	return arr[end]


arr = [4,5,7,8,9,10,13,15]
K = 5
X = 100
print(binarch_search(arr, 11))
print(find_closest_elements(arr, K, X))