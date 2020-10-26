"""
Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.


Note:
The string will only contain lowercase characters a-z.
The maximum length of the string is 50000.
"""


def validPalindrome(s: str) -> bool:
	if s == s[::-1]:
		return True
	left = 0
	right = len(s) - 1
	while left<right:
		if s[left] == s[right]:
			left += 1
			right -= 1
		else: break
	return s[left:right] == s[left:right][::-1] or s[left+1:right+1]==s[left+1:right+1][::-1]


s = "pidbliassaqozokmtgahluruufwbjdtayuhbxwoicviygilgzduudzgligyviciowxbhuyatdjbwfuurulhagtmkozoqassailbdip"

print(validPalindrome(s))
