"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.

"""

from typing import List


class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		from collections import defaultdict
		courses = defaultdict(list)

		for relation in prerequisites:
			next_course, prev_course = relation[0], relation[1]
			courses[prev_course].append(next_course)

		path = [False] * numCourses
		checked = [False] * numCourses
		for current_course in range(numCourses):
			if self.is_cyclic(current_course, courses, path, checked):
				return False
		return True

	def is_cyclic(self, current_course, courses, path, checked):
		"""
		backtracking method to check that no cycle would be formed starting from current_course
		"""
		if checked[current_course]:
			return False

		if path[current_course]:
			return True

		# before backtracking mark the node in the path
		path[current_course] = True

		# backtracking
		ret = False
		for child in courses[current_course]:
			ret = self.is_cyclic(child, courses, path, checked)
			if ret: break

		# after backtracking, remove the node from path
		path[current_course] = False
		checked[current_course] = True
		return ret
test = Solution()
numCourses =2
prerequisites = [[0,1], [1,0]]

print(test.canFinish(numCourses,prerequisites ))