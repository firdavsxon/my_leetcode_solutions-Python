"""
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]


Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.
"""
from typing import List


class Solution:
	def findAllConcatenatedWordsInADict(self, s: str, words: List[str]) -> List[int]:
		if len(words) == 0 or len(words[0]) == 0:
			return []
		words_frequency = {}
		for i in words:
			words_frequency[i] = words_frequency.get(i,0) + 1

		result_indices = []
		words_count = len(words)
		word_length = len(words[0])

		for i in range((len(s) - words_count*word_length)+1):
			words_seen = {}
			for j in range(0, words_count):
				next_word_index = i + j*word_length
				# get the next word from the string
				word = s[next_word_index:next_word_index+word_length]
				if word not in words_frequency: # break, we don't need this word
					break

				# Add the word to the 'word_seen' map
				if word not in words_seen:
					words_seen[word] = 0
				words_seen[word] += 1

				# No need to process further if the word has higher frequency required
				if words_seen[word]> words_frequency.get(word,0):
					break

				if j+1 == words_count: # Store index if we have found all words
					result_indices.append(i)

		return result_indices

test = Solution()
print(test.findAllConcatenatedWordsInADict("catfoxcat", ["cat", "fox"]))
print(test.findAllConcatenatedWordsInADict("wordgoodgoodgoodbestword", ["word","good","best","word"]))



