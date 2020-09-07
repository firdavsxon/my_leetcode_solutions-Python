"""
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""


class Solution:
	def length_of_longest_substring(self, s: str, k: int) -> int:
		window_start = 0
		max_length = 0
		d = {}
		max_repeat_letter_count = 0

		for window_end in range(len(s)):
			right = s[window_end]
			if right not in d:
				d[right] = 0
			d[right] += 1
			max_repeat_letter_count = max(max_repeat_letter_count, d[right])
			diff = window_end - window_start+1 - max_repeat_letter_count
			if diff > k:
				left = s[window_start]
				d[left] -= 1
				window_start += 1

			max_length  = max(max_length, window_end - window_start+1)
		return max_length

test =Solution()
print(test.length_of_longest_substring(s="aabccbb", k=2))
print(test.length_of_longest_substring(s="abbcb", k=1))
print(test.length_of_longest_substring(s="abccde", k=1))