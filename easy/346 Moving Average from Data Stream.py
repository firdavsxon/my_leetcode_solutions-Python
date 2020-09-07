"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""


class MovingAverage:

	def __init__(self, size: int):
		"""
		Initialize your data structure here.
		"""
		self.size = size
		self.l = []

	def next(self, val: int) -> float:
		self.l.append(val)
		if len(self.l) > self.size:
			self.l.pop(0)
		return sum(self.l) / len(self.l)

# Your MovingAverage object will be instantiated and called as such:
obj = MovingAverage(3)
param_1 = obj.next(110)
param_2 = obj.next(11)
param_4 = obj.next(12)
param_3 = obj.next(122)

