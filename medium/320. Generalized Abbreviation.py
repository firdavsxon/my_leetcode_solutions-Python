"""
A word's generalized abbreviation can be constructed by taking any number of non-overlapping and non-adjacent substrings and replacing them with their respective lengths.

For example, "abcde" can be abbreviated into:
"a3e" ("bcd" turned into "3")
"1bcd1" ("a" and "e" both turned into "1")
"5" ("abcde" turned into "5")
"abcde" (no substrings replaced)
However, these abbreviations are invalid:
"23" ("ab" turned into "2" and "cde" turned into "3") is invalid as the substrings chosen are adjacent.
"22de" ("ab" turned into "2" and "bc" turned into "2") is invalid as the substring chosen overlap.
Given a string word, return a list of all the possible generalized abbreviations of word. Return the answer in any order.



Example 1:

Input: word = "word"
Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]
Example 2:

Input: word = "a"
Output: ["1","a"]
"""

from typing import List
from collections import deque

class AbbreviatedWord:
	def __init__(self, string, start, count):
		self.string = string
		self.start = start
		self.count = count


class Solution:
	def generateAbbreviations(self, word: str) -> List[str]:
		word_length = len(word)
		result = []
		queue = deque()
		queue.append(AbbreviatedWord(list(), 0, 0))
		while queue:
			aw = queue.popleft()
			if aw.start == word_length:
				if aw.count != 0:
					aw.string.append(str(aw.count))
				result.append(''.join(aw.string))
			else:
				queue.append(AbbreviatedWord(list(aw.string), aw.start + 1, aw.count + 1))
				if aw.count != 0:
					aw.string.append(str(aw.count))
				new_word = list(aw.string)
				new_word.append(word[aw.start])
				queue.append(AbbreviatedWord(new_word, aw.start + 1, 0))

		return result


test = Solution()
print(test.generateAbbreviations("BAT"))



