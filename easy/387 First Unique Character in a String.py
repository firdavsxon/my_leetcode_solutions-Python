"""Given a string, find the first non-repeating character
in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.


Note: You may assume the string contains only lowercase English letters."""


class Solution:
	def firstUniqChar(self, s: str):
		# d={}
		# for i in range(len(s)):
		# 	if s[i] not in d:
		# 		d[s[i]]=1
		# 	else:
		# 		d[s[i]] += 1
		# for i in range(len(s)):
		# 	if s[i] in d and d[s[i]]==1:
		# 		return i
		# return -1
# ///////////////////////////////////////
		# d = {}
		# for i in range(len(s)):
		# 	if s[i] not in d:
		# 		d[s[i]] = 1
		# 	elif s[i] in d:
		# 		d[s[i]]+=1
		#
		# for i in range(len(s)):
		# 	if d[s[i]]==1:
		# 		return i
		# return -1
	# others:
		import string
		fc = len(s)
		for i in string.ascii_lowercase:   # string.ascii_lowercase is just lowercase english letter
			l = s.find(i)    # .find() function finds first existing symbol index
			if l != -1 and l == s.rfind(i): fc = min(l, fc) # rfind finds last existing symbol index
		return fc if fc != len(s) else -1

test = Solution()
print(test.firstUniqChar("leetcode"))
print(test.firstUniqChar("aadadaad"))


