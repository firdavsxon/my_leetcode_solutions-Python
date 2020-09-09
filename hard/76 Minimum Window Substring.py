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
