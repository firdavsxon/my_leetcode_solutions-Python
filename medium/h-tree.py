from math import sqrt

print("Practice makes Perfect!")


class Solution:
	def drawHTree(self, x, y, length, depth):
		if depth == 0:
			return
		x0 = x - length // 2
		x1 = x + length // 2
		y0 = y - length // 2
		y1 = y + length // 2

		self.drawline(x0, y0, x0, y1)
		self.drawline(x1, y0, x1, y1)
		self.drawline(x0, y, x1, y)

		new_length = length / sqrt(2)

		self.drawHTree(x0, y0, new_length, depth - 1)
		self.drawHTree(x0, y1, new_length, depth - 1)
		self.drawHTree(x1, y0, new_length, depth - 1)
		self.drawHTree(x1, y1, new_length, depth - 1)

	def drawline(self, x0, y0, x1, y1):
		print("Line is drawn by th endpoint: " + "(" + str(x0) + "," + str(y0) + ") " + "and " + "(" + str(x1) + "," + str(y1) + ")")

test = Solution()
test.drawHTree(0, 0 , 8, 2)


