"""
Write a function that reverses a string. The input string
is given as an array of characters char[].

Do not allocate extra space for another array, you must do
this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
from typing import List

class Solution:
	def reverseString(self, s: List[str]):
		"""
		Do not return anything, modify s in-place instead.
		"""
		n = len(s) - 1
		mid = n//2
		for i in range(mid+1):
			s[n - i], s[i] = s[i], s[n - i]
		return s
			
test = Solution()
print(test.reverseString(["h","e","l","l","o"]))
print(test.reverseString(["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a",
						  " ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]))

