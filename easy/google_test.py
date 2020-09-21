# Google
from typing import List

def utf8char_len(lst: List[bytes]):
	return len(lst)


print(utf8char_len(bytearray(11100000)))

import locale
print(locale.getpreferredencoding())