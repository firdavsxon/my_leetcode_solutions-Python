def minSubarray(arr, n, x):
	# Write your code here.
	#     1 2 3 4 5
	window_sum = 0

	min_length = float('inf')
	window_start = 0
	out = []

	for window_end in range(n):
		window_sum += arr[window_end]

		while (window_end - window_start + 1) >= 2 and window_sum > x:
			if min_length > window_end - window_start + 1:
				out = arr[window_start:window_end + 1]
			min_length = min(min_length, window_end- window_start +1)
			window_sum -= arr[window_start]
			window_start += 1

	return out

arr = [13, 7, 6, 12]
n = len(arr)
x = 13
print(minSubarray(arr, n , x))