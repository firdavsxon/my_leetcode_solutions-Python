"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106


"""
import heapq
from typing import List

class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:

		if not intervals:
			return 0

		intervals.sort(key=lambda x: x[0])
		# the heap initialization
		free_rooms = []
		heapq.heappush(free_rooms, intervals[0][1])

		for i in intervals[1:]:
			if free_rooms[0] <= i[0]:
				heapq.heappop(free_rooms)
			heapq.heappush(free_rooms, i[1])
		return len(free_rooms)
		# free_rooms.append(intervals[0][1])
#         for i in intervals[1:]:
#             if free_rooms[0]<= i[0]:
#                 free_rooms.sort(reverse=True)
#                 free_rooms.pop()
#             free_rooms.append(i[1])
#             free_rooms.sort()
# 		return len(free_rooms)
test = Solution()
intervals = [[0,30],[5,10],[15,20]]
print(test.minMeetingRooms(intervals))



