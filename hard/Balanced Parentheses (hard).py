"""
Problem Statement #
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

Example 1:

Input: N=2
Output: (()), ()()
Example 2:

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
((()))
"""
from collections import deque
class Solution:
	def generate_valid_parenthisis(self, num):
		result = []
		self.backtrack('', 0, 0, num, result)
		return result

	def backtrack(self, string, open, close, max, result):
		if len(string)==max*2:
			result.append(string)
			return
		if open<max:
			self.backtrack(string+"(", open+1, close, max, result)
		if close<open:
			self.backtrack(string+")", open, close+1, max, result)
test = Solution()

# print(test.generate_valid_parenthisis(5))

class ParenthesisString:
	def __init__(self, str, open_count, close_count):
		self.str = str
		self.open_count = open_count
		self.close_count = close_count

def generate(num):
	result = []
	queue = deque()
	queue.append(ParenthesisString('', 0, 0))
	while queue:
		ps = queue.popleft()
		if ps.open_count==num and ps.close_count==num:
			result.append(ps.str)
		else:
			if ps.open_count<num:
				queue.append(ParenthesisString(ps.str + "(", ps.open_count+1, ps.close_count))
			if ps.close_count<ps.open_count:
				queue.append((ParenthesisString(ps.str + ')', ps.open_count, ps.close_count+1)))
	return result

print(generate(3))