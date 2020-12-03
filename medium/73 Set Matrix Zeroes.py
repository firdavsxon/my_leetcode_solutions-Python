"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1

"""
from typing import List

class Solution:
	def setZeroes(self, matrix: List[List[int]]):
		"""
		Do not return anything, modify matrix in-place instead.
		"""
		n = len(matrix)
		m = len(matrix[0])
		zeros = []
		for i in range(n):
			for j in range(m):
				if matrix[i][j]==0:
					zeros.append([i,j])

		for zero in zeros:

			for row in range(n):
				for col in range(m):
					matrix[row][zero[1]]=0
					matrix[zero[0]][col] = 0
		return matrix





matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix1 = [[0,1,2,0],
		   [3,4,5,2],
		   [1,3,1,5]]
matrix2 = [[1,0]]

test = Solution()
func = test.setZeroes(matrix1)
print(func)