"""
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_start = 0
        max_length = 0
        substring={}

        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in substring:
                window_start = max(window_start, substring[right_char]+1)
            substring[right_char] = window_end
            max_length = max(max_length, window_end-window_start+1)
        return max_length


    def longest(self, s):
        frequency = {}
        max_length = window_start = 0

        # try to extend the range [window_start, window_end]
        for window_end in range(len(s)):
            # if the map already contains the "right char", shrink the window from beginning
            # so that we have only one occurrence of "right char"
            if s[window_end] in frequency:
                # update window start so if we have already latest character in map
                # move window start next character position
                window_start = max(window_start, frequency[s[window_end]] + 1)

            frequency[s[window_end]] = window_end  # insert next character to map
            # update last maximum length
            max_length = max(max_length, window_end-window_start+1)

        return max_length







test = Solution()
print(test.lengthOfLongestSubstring(s="aab"))
print(test.lengthOfLongestSubstring(s="abcabcbb"))
print(test.lengthOfLongestSubstring(s="bbbbb"))
print(test.lengthOfLongestSubstring(s="pwwkew"))
print(test.lengthOfLongestSubstring(s=""))
print(test.longest(s="bbbbb"))



