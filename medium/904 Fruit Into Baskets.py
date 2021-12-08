"""In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.


Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
"""
from typing import List

class Solution:
	def totalFruit(self, tree: List[int]) -> int:
		if not tree:
			return 0

		fruit_frequency={}
		maximum=0
		window_start = 0

		for window_end in range(len(tree)):
			right_fruit = tree[window_end]
			if right_fruit not in fruit_frequency:
				fruit_frequency[right_fruit] = 0
			fruit_frequency[right_fruit] += 1
			while len(fruit_frequency) > 2:
				left_fruit = tree[window_start]
				fruit_frequency[left_fruit] -= 1
				if fruit_frequency[left_fruit] == 0:
					del fruit_frequency[left_fruit]
				window_start += 1
			maximum = max(maximum, window_end-window_start + 1)
		return maximum

	def fruits_2(self, tree):
		if not tree: return 0

		fruits = {}
		window_start, max_fruit = 0, 0
		for idx, fruit in enumerate(tree):
			fruits[fruit] = fruits.get(fruit, 0) + 1
			while len(fruits)>2:
				fruits[tree[window_start]] -= 1
				if fruits[tree[window_start]] == 0:
					del fruits[tree[window_start]]
				window_start += 1
			max_fruit = max(max_fruit, idx - window_start +1)
		return max_fruit




test = Solution()
# print(test.totalFruit([1,2,1]))
print(test.totalFruit([0,1,2,2]))
# print(test.totalFruit(['A', 'B', 'C', 'A', 'C']))
print(test.fruits_2(['A', 'B', 'C', 'A', 'C']))

