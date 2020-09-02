"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.



Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true

"""


class Solution:
	def isStrobogrammatic(self, num: str) -> bool:
		lookup = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}

		lo, hi = 0, len(num) - 1

		while (lo <= hi):
			if num[lo] not in lookup or num[hi] not in lookup:
				return False
			elif num[lo] != lookup[num[hi]]:
				return False
			else:
				lo += 1
				hi -= 1
		return True

test = Solution()
print(test.isStrobogrammatic("69"))
print(test.isStrobogrammatic("96"))
print(test.isStrobogrammatic("88"))
print(test.isStrobogrammatic("77"))