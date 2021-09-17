from typing import List


def isValidSudoku(board: List[List[str]]):
	for i in range(9):
		d1 = {}
		d2 = {}
		for j in range(9):
			if board[i][j] != "." and board[i][j] not in d1:
				d1[board[i][j]] = 1
			elif board[i][j] != "." and board[i][j] in d1:
				return False

			if board[j][i] != "." and board[j][i] not in d2:
				d2[board[j][i]] = 1
			elif board[j][i] != "." and board[j][i] in d2:
				return False
	for i in range(0,9,3):
		for j in range(0,9,3):
			d3 = {}
			for k in range(3):
				for l in range(3):
					if board[i+k][i+l] !="." and board[i+k][i+l] not in d3:
						d3[board[i+k][i+l]] = 1
					elif board[i+k][i+l] !="." and board[i+k][i+l] in d3:
						return False
	return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))