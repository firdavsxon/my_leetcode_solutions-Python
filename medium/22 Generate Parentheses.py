"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]

Constraints:

1 <= n <= 8

"""

from typing import List
from collections import deque


class Parentheses:
	def __init__(self, string, open_count, close_count):
		self.string= string
		self.open_count = open_count
		self.close_count = close_count


class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		result = []
		queue = deque()
		queue.append(Parentheses("", 0, 0))
		while queue:
			ps = queue.popleft()
			# if we have reached the maximum number of open and close parentheses, add to the result
			if ps.open_count == n and ps.close_count == n:
				result.append(ps.string)
			else:
				if ps.open_count<n:   # if we can add open parentheses add it
					queue.append(Parentheses(
						ps.string + "(", ps.open_count+1, ps.close_count
					))
				if ps.open_count > ps.close_count:  # if we can add close parentheses add it
					queue.append(Parentheses(
						ps.string + ")", ps.open_count, ps.close_count + 1
					))
		return result


def generateParenthesis1( n: int) -> List[str]:
	result = []
	queue = deque()
	string = ''
	open_count = 0
	close_count = 0
	# queue.append(Parentheses("", 0 ,0))
	queue.append([string, open_count, close_count])

	while queue:
		ps = queue.popleft()

		if ps[1] == n and ps[2] == n:
			result.append(ps[0])
		else:
			if ps[1] < n:  # add open parentheses
				queue.append([ps[0] + "(", open_count + 1, ps[2]])
			# queue.append(Parentheses(
			# ps.string + "(", ps.open_count + 1, ps.close_count))
			if ps[1] > ps[1]:  # add closing parntheses
				# queue.append(Parentheses(ps.string + ")", ps.open_count, ps.close_count))
				queue.append([ps[0] + ")", ps[1], ps[2] + 1])
	return result

test = Solution()
# print(test.generateParenthesis(3))



# test myself

class P:
	def __init__(self, string, open_count, close_count):
		self.string = string
		self.open_count = open_count
		self.close_count = close_count


class S:
	def generate(self,  num):
		result = []
		queue = deque()
		queue.append(P("", 0,0))

		while queue:
			p = queue.popleft()
			if p.open_count == num and p.close_count == num:
				result.append(p.string)
			else:
				if p.open_count < num:
					queue.append(P(p.string+"(", p.open_count+1, p.close_count))
				if p.close_count < p.open_count:
					queue.append(P(p.string+")", p.open_count, p.close_count+1))
		return result

t =S()
print(t.generate(3))










