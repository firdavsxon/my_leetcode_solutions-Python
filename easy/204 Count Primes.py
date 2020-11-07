"""
Count the number of prime numbers less than a non-negative number, n.



Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
"""


class Solution:
	def countPrimes(self, n: int) -> int:
		counter = [1] * n
		counter[0:2] = [0, 0]
		start = 2
		while start ** 2 < n:
			if counter[start] == 1:
				for i in range(2 * start, n, start):
					counter[i] = 0
			start += 1
		return sum(counter)


test = Solution()
print(test.countPrimes(10))