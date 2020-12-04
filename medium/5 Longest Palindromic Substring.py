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

test = Solution()
s1= "lipwawibllrziekxgwudqghfpvsafguorthpsdihcinuasyzmttzxdluhrnfdrawabwxdgpoqabfhutzowqfhkynrhobyuygesngyxpjyilqhwyeemklicinmatyishobtitukbkpqtxwioqnztlewilnewokfqkycfuvgqmogwuvkrxphyjvhbkhpcwywfnazsoulmgdoaxyngoynmfexdcpanoyidutpzcicibjnzmybvggqbpbejsvliocotewgrfcwyebisiywjsugjxxwupryxglvkgdugbejsibuscjofrvaeexqweieldfhriftlczbuzmuizjqzxovziflaigwxrxowmhdlvrbxzeaaqxmicvigolodopbukjvkzwvxexnnweodsoscnpmuwgjhmlurwdqbwrzavjjubsueahunqwemmewqnuhaeusbujjvazrwbqdwrulmhjgwumpncsosdoewnnxexvwzkvjkubpodologivcimxqaaezxbrvldhmwoxrxwgialfizvoxzqjziumzubzcltfirhfdleiewqxeeavrfojcsubisjebgudgkvlgxyrpuwxxjgusjwyisibeywcfrgwetocoilvsjebpbqggvbymznjbiciczptudiyonapcdxefmnyognyxaodgmluoszanfwywcphkbhvjyhpxrkvuwgomqgvufcykqfkowenliweltznqoiwxtqpkbkutitbohsiytamnicilkmeeywhqliyjpxygnsegyuybohrnykhfqwoztuhfbaqopgdxwbawardfnrhuldxzttmzysaunichidsphtrougfasvpfhgqduwgxkeizrllbiwawpil"
s2= "babad"
print(test.longestPalindrome(s2))
