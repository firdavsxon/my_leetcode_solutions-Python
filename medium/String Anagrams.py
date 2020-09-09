"""
String Anagrams (hard) #
Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
Example 2:

Input: String="babcabc", Pattern="abc"
Output: [2, 3, 4]
Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".

"""


def find_string_anagrams(s, pattern):
	result_indexes = []
	window_start, matching_numbers = 0, 0
	ch_f = {}

	for char in pattern:
		if char not in ch_f:
			ch_f[char] = 0
		ch_f[char] += 1

	for window_end in range(len(s)):
		right = s[window_end]
		if right in ch_f:
			ch_f[right] -= 1
			if ch_f[right] == 0:
				matching_numbers += 1
		if matching_numbers == len(ch_f):
			result_indexes.append(window_start)

		if window_end >= len(pattern) - 1:
			left = s[window_start]
			window_start += 1
			if left in ch_f:
				if ch_f[left] == 0:
					matching_numbers -= 1
				ch_f[left] += 1
	return result_indexes


print(find_string_anagrams("ppqp", "pq"))
