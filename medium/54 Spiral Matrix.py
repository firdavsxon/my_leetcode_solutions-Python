"""

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

"""

from typing import List


class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		m = len(matrix)
		n = len(matrix[0])
		res = []
		Left = 0
		Right = n-1
		Bottom = m-1
		Top = 0
		# dr = 0
		while Top <= Bottom and Left <= Right:
			# if dr ==0:
			for i in range(Top, Right+1):
				res.append(matrix[Top][i])
			Top+=1
			# elif dr == 1:
			for i in range(Top,Bottom+1):
				res.append(matrix[i][Right])
			Right-=1
			# elif dr == 2:
			for i in range(Right, Left-1, -1):
				res.append(matrix[Bottom][i])
			Bottom-=1
			# elif dr == 3:
			for i in range(Bottom,Top-1, -1):
				res.append(matrix[i][Left])
			Left+=1
			# dr = (dr+1)%4
		return res
	
test = Solution()
print(test.spiralOrder([[1, 2, 3, 4, 5],
                        [6, 7, 8, 9, 10],
                        [11, 12, 13, 14, 15],
                        [16, 17, 18, 19, 20] ]))
# output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]






