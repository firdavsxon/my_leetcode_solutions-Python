def valid_solution(board):
	for i in range(len(board)):
		d1 = {}
		d2 = {}
		for j in range(len(board[i])):
			if board[i][j] not in d1:
				d1[board[i][j]] = 0
			elif board[i][j] in d1:
				return False

			if board[j][i] not in d2:
				d2[board[j][i]] = 0
			elif board[j][i] in d2:
				return False
	for i in range(0, len(board), 3):
		for j in range(0, len(board[i]), 3):
			d3 = {}
			for k in range(3):
				for l in range(3):
					if board[i + k][j + l] not in d3:
						d3[board[i + k][j + l]] = 0
					else:
						return False
	return True

def validSolution1(board):
	blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
	x=filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)
	return not x


print(validSolution1([[1, 2, 3, 4, 5, 6, 7, 8, 9],
					[2, 3, 4, 5, 6, 7, 8, 9, 1],
					[3, 4, 5, 6, 7, 8, 9, 1, 2],
					[4, 5, 6, 7, 8, 9, 1, 2, 3],
					[5, 6, 7, 8, 9, 1, 2, 3, 4],
					[6, 7, 8, 9, 1, 2, 3, 4, 5],
					[7, 8, 9, 1, 2, 3, 4, 5, 6],
					[8, 9, 1, 2, 3, 4, 5, 6, 7],
					[9, 1, 2, 3, 4, 5, 6, 7, 8]]))
print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
					[6, 7, 2, 1, 9, 5, 3, 4, 8],
					[1, 9, 8, 3, 4, 2, 5, 6, 7],
					[8, 5, 9, 7, 6, 1, 4, 2, 3],
					[4, 2, 6, 8, 5, 3, 7, 9, 1],
					[7, 1, 3, 9, 2, 4, 8, 5, 6],
					[9, 6, 1, 5, 3, 7, 2, 8, 4],
					[2, 8, 7, 4, 1, 9, 6, 3, 5],
					[3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
					[4, 9, 8, 2, 6, 1, 3, 7, 5],
					[7, 5, 6, 3, 8, 4, 2, 1, 9],
					[6, 4, 3, 1, 5, 8, 7, 9, 2],
					[5, 2, 1, 7, 9, 3, 8, 4, 6],
					[9, 8, 7, 4, 2, 6, 5, 3, 1],
					[2, 1, 4, 9, 3, 5, 6, 8, 7],
					[3, 6, 5, 8, 1, 7, 9, 2, 4],
					[8, 7, 9, 6, 4, 2, 1, 3, 5]]))
