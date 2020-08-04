"""
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.



Example 1:
Input: grid = [	[1,2,3],
				[4,5,6],
				[7,8,9]],    k = 1
Output: [[9,1,2],
		[3,4,5],
		[6,7,8]]

Example 2:

Input: grid = [	[3,8,1,9],
				[19,7,2,5],
				[4,6,11,10],
				[12,0,21,13]],    k = 4
Output: [	[12,0,21,13],
			[3,8,1,9],
			[19,7,2,5],
			[4,6,11,10]]

Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]


Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100

"""
from typing import List
from collections import deque


class Solution:
	# others
	def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

		# m = len(grid)
		# n = len(grid[0])
		# row_move = (k//n) % m
		# col_move = k % n
		#
		# result = []
		# if col_move>0:
		# 	for index, row in enumerate(grid):
		# 		result.append(grid[index-1][-col_move:] + grid[index][:-col_move])
		# else:
		# 	result = grid
		# return result[-row_move:] + result[:-row_move]

		m = len(grid)

		for i in range(k):
			grid_copy = grid[:]
			for j in range(m):
				if j == 0:
					# first element will be last item of original list ([grid_copy[m - 1][-1]]) plus other
					# elements of first list until last element (grid_copy[j][:-1])
					grid_copy[j] = [grid_copy[m - 1][-1]] + grid_copy[j][:-1]
				else:  # else next elem
					grid_copy[j] = [grid[j - 1][-1]] + grid[j][:-1]

			grid = grid_copy

		return grid


test = Solution()
print(test.shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
print(test.shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4))
