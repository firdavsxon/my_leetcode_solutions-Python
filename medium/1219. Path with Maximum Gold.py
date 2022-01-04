"""
n a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.


Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""
from typing import List


class Solution:

	def getMaximumGold(self, grid: List[List[int]]) -> int:
		if len(grid) < 1:
			return 0
		maximum = 0
		visited = [[False] * len(grid[0]) for _ in range(len(grid))]
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if grid[row][col] != 0:
					maximum = max(maximum, self.dfs(grid, row, col, visited))
		return maximum

	def dfs(self, grid, row, col, visited):
		if not self.out_boundary(grid, row, col) and grid[row][col] != 0 and visited[row][col] is False:
			visited[row][col] = True
			up = self.dfs(grid, row-1, col , visited)
			right = self.dfs(grid, row, col + 1, visited)
			down = self.dfs(grid, row + 1, col, visited)
			left = self.dfs(grid, row, col + 1, visited)
			visited[row][col] = False
			return max(up, max(down, max(left, right))+grid[row][col])
		else:
			return 0


	def out_boundary(self, grid, row, col):
		if row >= len(grid) or col >=len(grid[0]) or row < 0 or col < 0:
			return True
		return False

gold = Solution()
grid = [[0,6,0],
 	    [5,8,7],
 		[0,9,0]]
print(gold.getMaximumGold(grid))