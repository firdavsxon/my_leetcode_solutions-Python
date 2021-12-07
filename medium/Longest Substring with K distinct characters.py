"""
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

"""


class Solution:
	def __init__(self, string, k):
		self.string = string
		self.k = k

	def longest_substring_with_k(self):
		frequency  = {}
		output = 0
		window_start = 0
		for idx, character in enumerate(string):
			frequency[character] = frequency.get(character, 0) + 1

			while len(frequency)>k:
				frequency[string[window_start]]-=1
				if frequency[string[window_start]]==0:
					del frequency[string[window_start]]
				window_start+=1
			output = max(output, idx - window_start+1)
		return output



string = "cbbebi"
k = 3
test = Solution(string, k)

print(test.longest_substring_with_k())

