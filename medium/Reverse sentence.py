def reverse_words(arr):
	def reverseFunc(pArr, start, end):
		while start < end:
			pArr[start], pArr[end] = pArr[end], pArr[start]
			start += 1
			end -= 1

	L = len(arr)
	reverseFunc(arr, 0, L - 1)

	r = 0
	wordStart = None
	while r < L:
		if arr[r] == '  ':
			if wordStart is not None:
				reverseFunc(arr, wordStart, r - 1)
				wordStart = None
		elif r == L-1:
			if wordStart != None:
				reverseFunc(arr, wordStart, r)
		else:
			if wordStart is None:
				wordStart = r

		r += 1
	return arr


# arr = ['h', 'e', 'l', 'l', 'o']
# print(reverse_words(arr))

print(reverse_words(['p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
					 'm', 'a', 'k', 'e', 's', '  ',
					 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']))
