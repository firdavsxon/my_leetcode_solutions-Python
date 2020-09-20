# Google
def utf8char_len(lst: bytes):
	start = 0
	count = 0
	end = len(lst) - 1
	while start <= end:
		if start == 0 and lst[start] == 0:
			if 1 in lst[1:]:
				return 1
			else:
				return 0
		elif start == 0 and lst[start] == 1:
			start += 1
			count += 1
		elif lst[start] == 0:
			return count


print(utf8char_len(10101010))
