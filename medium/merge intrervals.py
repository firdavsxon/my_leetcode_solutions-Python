"""

Problem Statement #
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
one [1,5].
svg viewer
Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
	if len(intervals) < 2:
		return intervals
	merged_intervals = []
	start = intervals[0][0]
	end = intervals[0][1]

	for i in range(1, len(intervals)):
		temp_interval = intervals[i]
		if temp_interval[0] <= end:
			end = max(temp_interval[1], end)
		else:
			merged_intervals.append([start, end])
			start = temp_interval[0]
			end = temp_interval[1]
	merged_intervals.append([start, end])
	return merged_intervals


intervals0 = [[1,4], [2,5], [7,9]]
intervals= [[6,7], [2,4], [5,9]]
print(merge(intervals0))
print(merge(intervals))