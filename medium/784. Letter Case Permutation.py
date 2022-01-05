"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.



Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]

"""
from typing import List
from collections import deque

class Solution:
	def letterCasePermutation(self, s: str) -> List[str]:
		permutations = [s]
		for i, ch in enumerate(s):
			if ch.isalpha():
				n = len(permutations)
				for j in range(n):
					temp = list(permutations[j])
					temp[i] = temp[i].swapcase()
					permutations.append(''.join(temp))

		return permutations


test = Solution()
s= "abc"
print(test.letterCasePermutation(s))


"""

rr = ['cc32', 'D45', 'DDD434', 'asQA8789', 'dssSDSD822']
arr1 = ['C4', 'C45','c4', 'C5434']
arr2 = ['Abel', 'ab', 'aAA']

sorted_list = sorted(arr1, key=str.casefold)
print(sorted_list)

def mysort(arr):
	for i, num in enumerate(arr):
		left = i
 
"""