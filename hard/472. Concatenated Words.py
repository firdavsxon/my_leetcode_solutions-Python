"""

Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.



Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]


Constraints:

1 <= words.length <= 104
0 <= words[i].length <= 1000
words[i] consists of only lowercase English letters.
0 <= sum(words[i].length) <= 105

"""


class Solution:
	def findall_concatenation(self, string, words):
		if len(words) == 0 or len(words[0]) == 0:
			return []

		word_frequency = {}

		for word in words:
			word_frequency[word] = word_frequency.get(word, 0) +1

		result_indices = []
		words_count = len(words)
		word_length = len(words[0])

		for i in range((len(string) - words_count*word_length)+1):
			words_seen = {}
			for j in range(words_count):
				next_word_index = i + j*word_length
				# get the next word from string
				word = string[next_word_index: next_word_index + word_length]
				if word not in word_frequency: #break if we do not need this word
					break
				# add the word to the "words_seen" map
				if word not in words_seen:
					words_seen[word] = 0
				words_seen[word] += 1

				#No need to process further if the word has higher frequency than required
				if words_seen[word] > word_frequency.get(word,0):
					break
				if j +1 == words_count: # stroe indexes if we found all required
					result_indices.append(i)
		return result_indices






test = Solution()
String="catfoxcat"
Words=["cat", "fox"]

print(test.findall_concatenation(String, Words))