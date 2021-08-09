""":cvar
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.



Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Example 3:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]
Example 4:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]
Example 5:

Input: list1 = ["KFC"], list2 = ["KFC"]
Output: ["KFC"]
"""
from typing import List

class Solution:
	def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
		d1 = {}
		d2 = {}
		for idx, i in enumerate(list1):
			if i not in d1:
				d1[i] = idx
		for idx, i in enumerate(list2):
			if i not in d2:
				d2[i] = idx
		out = {}
		for key, val in d1.items():
			if key in d2:
				out[key] = val + d2[key]
		output = []
		least_index = min(out.values())
		for key, val in out.items():
			if val == least_index:
				output.append(key)
		return output

test = Solution()
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(test.findRestaurant(list1, list2))