"""
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),


#  xerexs
"""
from itertools import islice


class Solution:
	def longestPalindrome(self, s: str) -> str:
		def expand_around_center(s: str, left: int, right: int):
			L, R = left, right
			while L >= 0 and R<len(s) and s[L] == s[R]:
				L-=1
				R+=1
			return R-L-1

		start, end = 0, 0
		for window_end, ch in enumerate(s):
			l1 = expand_around_center(s, window_end, window_end)
			l2 = expand_around_center(s, window_end, window_end+1)
			l = max(l1,l2)
			if l > end-start:
				start = window_end - (l-1)//2
				end = window_end+l//2
		return s[start: end+1]
	# longest palindrom substring with Manachers algorithm

	def longest_palindrome(self, s: str) -> str:
		if len(s) < 2:
			return s
		processed_string = "#".join("^{}S".format(s))
		length = len(processed_string)
		lps = [0]*length
		center = right = max_lps_length = max_lps_position = 0

		for offset,_ in islice(enumerate(processed_string),1, length-1):
			print(offset)

			# check of within previous range of previous largest palindrome

			if offset< right:
				lps[offset] = min(lps[2*center - offset], right - offset)

			# check if within previous range and if so, expand from current character to left and right and compare them
			while (offset + lps[offset] + 1 < length
					and offset - lps[offset]-1>0
					and processed_string[offset + lps[offset]+1] == processed_string[(offset - lps[offset]-1)]):
				lps[offset] += 1

			if lps[offset] > max_lps_length:
				max_lps_length = lps[offset]
				max_lps_position = offset

			if offset + lps[offset]> right:
				center = offset
				right = offset + lps[offset]
		start = (max_lps_position - max_lps_length)//2
		end = start + max_lps_length - 1
		return s[start:end+1]










test = Solution()
s1= "lipwawibllrziekxgwudqghfpvsafguorthpsdihcinuasyzmttzxdluhrnfdrawabwxdgpoqabfhutzowqfhkynrhobyuygesngyxpjyilqhwyeemklicinmatyishobtitukbkpqtxwioqnztlewilnewokfqkycfuvgqmogwuvkrxphyjvhbkhpcwywfnazsoulmgdoaxyngoynmfexdcpanoyidutpzcicibjnzmybvggqbpbejsvliocotewgrfcwyebisiywjsugjxxwupryxglvkgdugbejsibuscjofrvaeexqweieldfhriftlczbuzmuizjqzxovziflaigwxrxowmhdlvrbxzeaaqxmicvigolodopbukjvkzwvxexnnweodsoscnpmuwgjhmlurwdqbwrzavjjubsueahunqwemmewqnuhaeusbujjvazrwbqdwrulmhjgwumpncsosdoewnnxexvwzkvjkubpodologivcimxqaaezxbrvldhmwoxrxwgialfizvoxzqjziumzubzcltfirhfdleiewqxeeavrfojcsubisjebgudgkvlgxyrpuwxxjgusjwyisibeywcfrgwetocoilvsjebpbqggvbymznjbiciczptudiyonapcdxefmnyognyxaodgmluoszanfwywcphkbhvjyhpxrkvuwgomqgvufcykqfkowenliweltznqoiwxtqpkbkutitbohsiytamnicilkmeeywhqliyjpxygnsegyuybohrnykhfqwoztuhfbaqopgdxwbawardfnrhuldxzttmzysaunichidsphtrougfasvpfhgqduwgxkeizrllbiwawpil"
s2= "babad"
print(test.longest_palindrome(s2))
