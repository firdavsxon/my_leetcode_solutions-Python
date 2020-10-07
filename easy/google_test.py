# Google
from typing import List


def utf8char_len(lst: List[bytes]):
	for i in range(1, len(lst)):
		if lst[i][0] != '1' and lst[i][1] != '0':
			return 'Error'
	for i in range(len(lst[0])):
		count = 0
		while lst[i] != '0':
			count >>= lst[i]
			if i == len(lst) - 1 and lst[i] == '1':
				return '8'

	return count


def count_bits(n):
	num_of_bits = 0

	while n:
		num_of_bits ^= n & 1
		n >>= 1
	return num_of_bits


print(count_bits(1010))

print(utf8char_len([b'1110XXXX', b'10000000', b'10000000']))
