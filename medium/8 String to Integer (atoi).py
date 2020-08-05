"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters
as necessary until the first non-whitespace character is found.
 Then, starting from this character, takes an optional initial plus
 or minus sign followed by as many numerical digits as possible,
 and interprets them as a numerical value.

The string can contain additional characters after those
that form the integral number, which are ignored and have no
effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is
not a valid integral number, or if no such sequence exists
because either str is empty or it contains only whitespace
characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−231,  231 − 1].
If the numerical value is out of the range of representable values,
INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""
import re


class Solution:
	def myAtoi(self, str: str) -> int:
		# str = str.strip()
		# num = 0
		# ret_num = ''
		# for i in range(len(str)):
		# 	if i == 0 and not str[i].isnumeric() and str[i] not in ['-', '+']:
		# 		return 0
		# 	elif i == 0 and str[i] == '-':
		# 		num = -1
		# 	elif i == 0 and str[i] == '+':
		# 		continue
		# 	elif not str[i].isnumeric():
		# 		ret_num = str[:i]
		# 		break
		# 	if str[i].isnumeric():
		# 		ret_num += (str[i])
		#
		#
		# # str = "".join(re.findall("[0-9]", str))
		#
		# if ret_num == '':
		# 	return 0
		# ret_num = int(ret_num)
		# if num == -1:
		# 	ret_num *= -1
		# if ret_num < (-(2 ** 31)):
		# 	return -2147483648
		# if ret_num > ((2 ** 31) - 1):
		# 	return (2 ** 31) - 1
		# return ret_num

		str = str.strip()
		if len(str) == 0:
			return 0
		num = 0
		for i in range(len(str)):
			if i == 0 and not str[i].isnumeric() and str[i] not in ['-', "+"]:
				return 0
			elif i == 0 and str[i] == '-':
				num = -1
			elif i == 0 and str[i] == '+':
				continue
			elif not str[i].isnumeric():
				str = str[:i]
				break
		str = "".join(re.findall("[0-9]", str))
		if str == '':
			return 0
		ret_num = int(str)
		if num == -1:
			ret_num *= -1
		return min(max(ret_num, -2**31), 2**31-1)

	def myAtoi1(self, str: str) -> int:

		s = s1 = ""
		res = 0

		str = str.strip()
		i = 0
		if not str: return 0

		if str[0] in '+-':
			s1 += str[0]
			i = 1

		for x in range(i, len(str)):
			if str[x].isdigit():
				s += str[x]
			else:
				break

		if len(s) > 0:
			res = int(s1 + s)

		if res > 2 ** 31 - 1:
			return 2 ** 31 - 1
		elif res < -2 ** 31:
			return -2 ** 31
		else:
			return res


test = Solution()
print(test.myAtoi1("42"))
# print(test.myAtoi("    -42"))
# print(test.myAtoi("4193 with words"))
# print(test.myAtoi("words and 987"))
# print(test.myAtoi("-91283472332"))
# print(test.myAtoi("3.14159"))
print(test.myAtoi1("+-1"))
