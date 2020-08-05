"""

Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution:
	def isPalindrome(self, s: str) -> bool:
		# if len(s) == 0:
		# 	return True
		# for i in s:
		# 	if not i.isalnum():
		# 		s=s.replace(i, '')
		# s.strip()
		# n=len(s)-1
		# mid=n//2
		# for i in range(mid+1):
		#
		# 	if s[i].lower() != s[n-i].lower():
		# 		return False
		# return True
		if len(s) == 0:
			return True
		x = []
		for i in s:
			if i.isalnum():
				x.append(i)
		n = len(x) - 1
		mid = n // 2
		for i in range(mid + 1):
			if x[i].lower() != x[n - i].lower():
				return False
		return True

test = Solution()
# print(test.isPalindrome("A man, a plan, a canal: Panama"))
# print(test.isPalindrome("race a car"))
print(test.isPalindrome("0P"))

