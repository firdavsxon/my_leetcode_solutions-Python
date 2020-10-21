"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.

"""
from typing import List
filename= __file__
breakpoint()
print(f"path={filename}")

class Solution:
	def isValidSudoku(self, board: List[List[str]]):

		for i in range(len(board)):
			d1 = {}
			d2 = {}

			for j in range(len(board[i])):
				if board[i][j] != '.':
					if board[i][j] not in d1:
						d1[board[i][j]] = 1
					else:
						return False
				if board[j][i] != '.':
					if board[j][i] not in d2:
						d2[board[j][i]] = 1
					else:
						return False
		for i in range(0, len(board), 3):
			for j in range(0, len(board), 3):
				d3 = {}
				for k in range(3):
					for l in range(3):
						if board[i + k][j + l] != '.':
							if board[i + k][j + l] not in d3:
								d3[board[i + k][j + l]] = i
							else:
								return False

		return True

	# others

	def others_solution1(self, board: List[List[str]]) -> bool:
		rowSet = [set() for i in range(len(board))]
		colSet = [set() for i in range(len(board))]

		squareSets = [[set() for _ in range(3)] for _ in range(3)]

		for i in range(9):
			for j in range(9):
				x = board[i][j]

				if x == ".":
					continue

				# Handle rows
				if x in rowSet[i]:
					return False
				rowSet[i].add(x)

				# Handle columns
				if x in colSet[j]:
					return False
				colSet[j].add(x)

				# Handle squares
				rowSquare = i // 3
				colSquare = j // 3

				if x in squareSets[rowSquare][colSquare]:
					return False
				squareSets[rowSquare][colSquare].add(x)

		return True

	""" Optimal solution """

	def others_solution2(self, board: List[List[str]]) -> bool:
		"""Points to consider - works since val is not an int"""
		valuesSet = []

		for i, row in enumerate(board):

			for j, val in enumerate(row):

				if val != '.':
					valuesSet.extend(((i, val), (val, j), (i // 3, j // 3, val)))

		return len(valuesSet) == len(set(valuesSet))


test = Solution()
print(test.isValidSudoku([[".", ".", ".", "8", ".", ".", ".", ".", "."],
						  [".", ".", ".", ".", ".", ".", ".", ".", "."],
						  [".", "6", ".", ".", ".", ".", "3", ".", "."],
						  ["7", ".", ".", "9", "6", "4", "1", ".", "."],
						  ["6", ".", "9", ".", ".", ".", ".", ".", "."],
						  [".", ".", ".", ".", ".", ".", ".", "5", "."],
						  [".", ".", "9", ".", ".", ".", ".", ".", "."],
						  [".", ".", ".", ".", ".", ".", ".", ".", "5"],
						  [".", ".", "1", ".", ".", ".", ".", "2", "."]]))
print(test.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
						  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
						  [".", "9", "8", ".", ".", ".", ".", "6", "."],
						  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
						  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
						  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
						  [".", "6", ".", ".", ".", ".", "2", "8", "."],
						  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
						  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

print(test.isValidSudoku([[".", "2", "3", "4", "5", "6", "7", "8", "9"],
						  ["1", ".", ".", ".", ".", ".", ".", ".", "."],
						  [".", ".", ".", ".", ".", ".", ".", ".", "."],
						  [".", ".", ".", ".", ".", ".", ".", ".", "."],
						  [".", ".", ".", ".", ".", ".", ".", ".", "."],
						  [".", ".", ".", ".", ".", ".", ".", ".", "."],
						  [".", ".", ".", ".", ".", ".", ".", ".", "."],
						  [".", ".", ".", ".", ".", ".", ".", ".", "."],
						  [".", ".", ".", ".", ".", ".", ".", ".", "."]]))
