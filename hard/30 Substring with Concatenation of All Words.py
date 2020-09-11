"""
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Note:

The number of elements of the given array will not exceed 10,000
The length sum of elements in the given array will not exceed 600,000.
All the input string will only include lower case letters.
The returned elements order does not matter.

"""
from typing import List


class Solution:
	def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
		if len(words) == 0 or len(words)[0] == 0:
			return []
		words_frequency = {}
		for i in words:
			words_frequency[i] = words_frequency.get(i,0) + 1

		result_indeces = []
		words_count = len(words)
		word_length = len(words)[0]

		for i in range(len(words)):



