from heapq import *


def sort_k_messed_array(arr, k):
	min_heap = []
	for idx, current in enumerate(arr):
		i = 0
		while i <= k and idx+i < len(arr) :
			heappush(min_heap, (arr[idx+i], idx+i))
			i += 1
		current = heappop(min_heap)
		if current[0]<arr[idx]:
			arr[idx], arr[current[1]] = arr[current[1]], arr[idx]
		min_heap = []
	return arr

arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k=2
print(sort_k_messed_array(arr, k))