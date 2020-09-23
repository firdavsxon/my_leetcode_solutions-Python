# Google
from typing import List

def utf8char_len(lst: List[bytes]):
	length = 0
	for num in lst:
		bin_repr = format(num, '#010b')[-8:]
		t = type(bin_repr)
		for bit in bin_repr:
			if bit== '0': break
			length += 1
	return length


print(utf8char_len(0b10011001))

