"""
Problem Statement #
Given an array of points in the a 2D2D plane, find ‘K’ closest points to the origin.

Example 1:

Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.
Example 2:

Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]
"""
from heapq import *
from math import sqrt
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Solution:

	def find_closest_point(self, points, k):
		min_heap = []
		total = {}
		result = []

		for point in points:
			euc = (point.x)**2 + (point.y)**2
			total[(point.x, point.y)] = euc
		values = [val for key, val in total.items()]
		for i in range(k):
			heappush(min_heap, -values[i])

		for i in range(k, len(values)):
			if values[i]<-min_heap[0]:
				heappop(min_heap)
				heappush(min_heap, -values[i])

		for number in min_heap:
			for key, val in total.items():
				if -number==val:
					result.append(list(key))
		return result




test = Solution()
points = [Point(1,3),Point(3,4), Point(2,-1)]
k = 2
print(test.find_closest_point(points, k))