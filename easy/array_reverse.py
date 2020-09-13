
arr2 = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
        'm', 'a', 'k', 'e', 's', '  ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

arr1= [' ', ' ']

def rev(arr):
	n = len(arr)-1
	rev_mirror(arr, 0 , n)

	word_start = None
	for i in range(n-1):
		if arr[i] == '  ':
			if word_start is not None:
				rev_mirror(arr, word_start, i-1)
				word_start = None
		elif i == n-1:
			if word_start is not None:
				rev_mirror(arr, word_start, i)
		else:
			if word_start is None:
				word_start = i

	return arr


def rev_mirror(arr, left, right):

	while left < right:
		arr[left], arr[right] = arr[right], arr[left]
		left += 1
		right -= 1
	return arr

print(rev(arr1))
