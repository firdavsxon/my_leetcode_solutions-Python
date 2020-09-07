"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

"""

class Solution:
	def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
		window_start = 0
		max_length = 0
		d={}
		
		for window_end in range(len(s)):
			right = s[window_end]
			d[right] = window_end
			
			while len(d) > k:
				left = s[window_start]
				d[left] -= 1
				if d[left] == 0:
					del d[left]
				window_start +=1
			max_length = max(max_length, window_end-window_start +1)
		return max_length

test = Solution()
print(test.lengthOfLongestSubstringKDistinct(s="eceba", k=2))
print(test.lengthOfLongestSubstringKDistinct(s = "aa", k = 1))
			