"""

Problem Statement #
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".

"""


class Solution:
	def no_repeat(self, string):
		window_start = 0
		max_length = 0
		frequency = {}

		for window_end in range(len(string)):
			right_char = string[window_end]
			if right_char in frequency:
				window_start = max(window_start, frequency[right_char] +1)
			frequency[right_char] = window_end

			max_length = max(max_length, window_end - window_start + 1)
		return max_length

obj = Solution()
string = "aabccbb"
print(obj.no_repeat(string))