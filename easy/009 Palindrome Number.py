# Palindrome Number

"""
Determine whether an integer is a palindrome. An integer
is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?

"""


class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x < 0:
			return False
		s = str(x)
		if s == s[::-1]:
			return True
		return False

	def isPalindromeNoStr(self, x: int) -> bool:
		q = x
		rev = 0
		if x < 0:
			return False

		while x > 0:
			reminder = x % 10
			rev = rev * 10 + reminder
			x = x // 10
		return rev == q


test = Solution()
print(test.isPalindromeNoStr(121))
print(test.isPalindromeNoStr(1234321))
print(test.isPalindromeNoStr(234))


# logic can be found here: https://www.techiedelight.com/determine-given-number-palindrome-not/
