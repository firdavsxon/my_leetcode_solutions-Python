"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:

Input: "()"
Output: True
Example 2:

Input: "(*)"
Output: True
Example 3:

Input: "(*))"
Output: True
"""

class Solution:
	def checkValidString(self, s: str) -> bool:
		l, w = 0, 0

		for i in s:
			if i == '(':
				l += 1
			elif i== ')':
				l -= 1
				if l < 0:
					if l+w < 0:
						return False
					w -= 1
					l = 0
			else:
				w += 1

		r, w = 0, 0

		for i in s[::-1]:
			if i == ')':
				r += 1
			elif i == '(':
				r -= 1
				if r < 0:
					if r+w < 0:
						return False
					w -= 1
					r = 0
			else: w += 1
		return True

test = Solution()
print(test.checkValidString('((((*))))'))
print(test.checkValidString('((()'))
print(test.checkValidString('(*))'))
print(test.checkValidString('((*))'))