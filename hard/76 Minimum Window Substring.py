"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


class Solution:
	def minWindow(self, s: str, t: str) -> str:
		window_start, matched, sub_start = 0, 0, 0
		min_length = len(s)+1
		subs = {}

		for p in t:
			if p not in subs:
				subs[p] = 0
			subs[p] += 1

		for window_end in range(len(s)):
			right = s[window_end]
			if right in subs:
				subs[right]-=1
				if subs[right] >= 0:
					matched += 1
			while matched == len(t):
				if min_length > window_end-window_start+1:
					min_length = window_end-window_start+1
					sub_start = window_start
				left = s[window_start]
				window_start += 1
				if left in subs:
					if subs[left] == 0:
						matched -= 1
					subs[left] += 1
		if min_length > len(s):
			return ''
		return s[sub_start:sub_start+min_length]


test = Solution()
print(test.minWindow("ADOBECODEBANC", "ABC"))


def number_modify(lst, pos):
	last_zero_pos = float('-inf')
	for idx, num in enumerate(lst):
		if num == '0' and idx > pos:
			last_zero_pos = idx
	if last_zero_pos != float('-inf'):
		lst[0], lst[last_zero_pos] = lst[last_zero_pos], lst[0]


def asteriks_modify(lst, position):
	lst[position - 2], lst[position - 1] = lst[position - 1], lst[position - 2]
	lst = lst[:position] + lst[position + 1:]
	return lst


def decryptPassword(s):
	print(s)
	numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	s_list = [i for i in s]
	print(s_list)
	i = 0
	while i < len(s_list):
		if s_list[i] in numbers:
			number_modify(s_list, i)
		elif s_list[i] == "*":
			s_list = asteriks_modify(s_list, i)
		i +=1
	for i in reversed(s_list):
		if i == '0':
			s_list.pop(i)

	return ''.join(s_list)


