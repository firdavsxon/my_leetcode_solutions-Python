"""

Write program that takes two arrays representing integers, and returns an integer
representing their product. For example, [1, 9, 3, 7, 0, 7, 7, 2, 1] represents 193707721 and
[-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7] represents -761838257287. Since
193707721 x -761838257287 = -147573952589676412927, your function should
return th following array [-1, 4, 7, 5, 7, 3, 9, 5, 2, 5, 8, 9, 6, 7, 6, 4, 1, 2, 9, 2, 7]

"""
from typing import List


def multiply(num1: List[int], num2: List[int]) -> List[int]:
	sign = -1 if num1[0] < 0 or num2[0] < 0 else 1
	num1[0], num2[0] = abs(num1[0]), abs(num2[0])

	res = [0] * (len(num1) + len(num2))
	for i in reversed(range(len(num1))):
		for j in reversed(range(len(num2))):
			res[i + j + 1] += num1[i] * num2[j]
			res[i + j] += res[i + j + 1] // 10
			res[i + j + 1] %= 10
	# remove the leading zeros
	res = res[next((i for i, x in enumerate(res) if x != 0), len(res)):] or [0]
	return [sign * res[0]] + res[1:]

print(multiply([1,2,3], [9,8,7]))
print(multiply([1, 2, 3, 4, 5], [-1, 3, 45, 5, 6, 7, 8, 9, 98]))
