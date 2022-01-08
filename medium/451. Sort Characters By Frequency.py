"""

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.



Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
from heapq import *
from collections import Counter


class Solution:
	def frequencySort(self, s: str) -> str:
		count =Counter(s)
		min_heap = []
		for character, frequency in count.items():
			heappush(min_heap, (frequency, character))
		out = []
		while min_heap:
			current = heappop(min_heap)
			for _ in range(current[0]):
				out.append(current[1])
		return ''.join(out[::-1])





test = Solution()
string = 'tree'
print(test.frequencySort(string))
