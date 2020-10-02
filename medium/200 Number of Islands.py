"""

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

"""
from typing import List


class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		def dfs(matrix, r, c):
			nr = len(matrix)
			nc = len(matrix[0])

			if r < 0 or c < 0 or r >= nr or c >= nc or matrix[r][c] == '0':
				return
			matrix[r][c] = '0'
			dfs(matrix, r - 1, c)
			dfs(matrix, r + 1, c)
			dfs(matrix, r, c - 1)
			dfs(matrix, r, c + 1)

		if not grid:
			return 0

		nr = len(grid)
		nc = len(grid[0])
		num_islands = 0

		for r in range(nr):
			for c in range(nc):
				if grid[r][c] == '1':
					num_islands += 1
					dfs(grid, r, c)
		return num_islands
	
test = Solution()
print(test.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))