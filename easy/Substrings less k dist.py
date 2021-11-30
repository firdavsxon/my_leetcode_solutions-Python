def subStringsLessKDist(inputString, num):
	window_start = 0
	res = []

	# hash_map = {}
	window_end = num
	while window_end < len(inputString):
		# right_char = inputString[window_end]
		# if right_char not in hash_map:
		# 	hash_map[right_char] = 0
		# else:
		# 	hash_map[right_char] += 1
		#
		# if len(hash_map) == num - 1:
		# 	if (window_end - window_start + 1) == num:
		# 	res.append(inputString[window_start:window_end + 1])
		# 	del hash_map[inputString[window_start]]
		# if len(hash_map) == num - 1 and len(hash_map) != num - 1:
		# 	del hash_map[inputString[window_start]]
		# 	window_start += 1
		if (window_end - window_start +1) == num+1 and len(set(inputString[window_start:window_end]))==num-1:
			res.append(inputString[window_start:window_end])
			window_start+=1
			window_end+=1
		else:
			window_start+=1
			window_end+=1

	return res


print(subStringsLessKDist("wawaglknagagwunagkwkwagl", 4))

def subStringsLessKDist1(inputString, num):
	window_start = 0
	res = []

	hash_map = {}
	window_end = num
	while window_end < len(inputString)+1:
		# right_char = inputString[window_end]
		# if right_char not in hash_map:
		# 	hash_map[right_char] = 0
		# else:
		# 	hash_map[right_char] += 1
		#
		# if len(hash_map) == num - 1:
		# 	if (window_end - window_start + 1) == num:
		# 	res.append(inputString[window_start:window_end + 1])
		# 	del hash_map[inputString[window_start]]
		# if len(hash_map) == num - 1 and len(hash_map) != num - 1:
		# 	del hash_map[inputString[window_start]]
		# 	window_start += 1
		if (window_end - window_start +1) == num+1 and len(set(inputString[window_start:window_end]))==num-1:
			res.append(inputString[window_start:window_end])
		window_start+=1
		window_end+=1


	return res


print(subStringsLessKDist1("democracy", 5))
print(subStringsLessKDist1("wawaglknagagwunagkwkwagl", 4))
print(subStringsLessKDist1("", 4))
