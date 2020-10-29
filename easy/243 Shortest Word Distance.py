"""
Given a list of words and two words word1 and word2, return the shortest
distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2
are both in the list.
"""
from typing import List

class Solution:
	def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
		idx1 = float('inf')
		idx2 = float('inf')
		distance = float('inf')
		for idx, word in enumerate(words):
			if word == word1:
				idx1 = idx
			if word == word2:
				idx2 = idx
			distance = min(distance, abs(idx2 - idx1))
		return distance
