""":Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?"""


class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		d1 = {}
		d2 = {}
		for i in s:
			if i not in d1:
				d1[i] = 1
			else:
				d1[i] += 1
		for i in t:
			if i not in d2:
				d2[i] = 1
			else:
				d2[i] += 1

		if d1 == d2:
			return True
		return False
test = Solution()
print(test.isAnagram("ab","ba"))
print(test.isAnagram(s = "anagram", t = "nagaram"))
print(test.isAnagram(s = "rat", t = "car"))
