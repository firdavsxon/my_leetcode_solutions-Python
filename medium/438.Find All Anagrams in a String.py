"""

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

class Solution:
	def find_anagram_indexes(self, s, p):
		left =0
		matched = 0
		frequency = {}
		out = []
		for char in p:
			frequency[char] = frequency.get(char, 0) + 1

		for right, char in enumerate(s):
			if char in frequency:
				frequency[char] -=1
				if frequency[char] == 0:
					matched +=1
			if matched == len(frequency):
				out.append(left)

			if right >= len(p) -1:
				left_char = s[left]
				left +=1

				if left_char in frequency:
					if frequency[left_char] == 0:
						matched -=1
					frequency[left_char] +=1
		return out



test = Solution()
s = "cbaebabacd"
p = "abc"
print(test.find_anagram_indexes(s,p))