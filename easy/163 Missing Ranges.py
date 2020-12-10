"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"
Example 2:

Input: nums = [], lower = 1, upper = 1
Output: ["1"]
Explanation: The only missing range is [1,1], which becomes "1".
Example 3:

Input: nums = [], lower = -3, upper = -1
Output: ["-3->-1"]
Explanation: The only missing range is [-3,-1], which becomes "-3->-1".
Example 4:

Input: nums = [-1], lower = -1, upper = -1
Output: []
Explanation: There are no missing ranges since there are no missing numbers.
Example 5:

Input: nums = [-1], lower = -2, upper = -1
Output: ["-2"]


Constraints:

-10**9 <= lower <= upper <= 10**9
0 <= nums.length <= 100
lower <= nums[i] <= upper
All the values of nums are unique.

"""
from typing import List

class Solution:
	def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
		def helper(nums, lo,up):
			if lo==up:
				nums.append(str(lo))
			else:
				nums.append((str(lo)+"->"+str(up)))
		output = []
		if len(nums)<1:
			helper(output, lower, upper)
			return output
		low= float('inf')
		for i in range(lower, upper+1):
			if i not in nums:
				low = min(low, i)
				if i+1 in nums:
					up=i
					helper(output, low,up)
					low = float('inf')
				if i==upper:
					helper(output, low, upper)

		return output

	def findMissingRanges1(self, nums: List[int], lower: int, upper: int) -> List[str]:
		def helper(nums, lo,up):
			if lo==up:
				nums.append(str(lo))
			else:
				nums.append((str(lo)+"->"+str(up)))
		output = []
		if len(nums)<1:
			helper(output, lower, upper)
			return output
		if nums[0]>lower:
			helper(output, lower, nums[0]-1)
		for i in range(1, len(nums)):
			if nums[i] - nums[i-1]>1:
				helper(output, nums[i-1]+1, nums[i]-1)
		if nums[len(nums)-1] <upper:
			helper(output, nums[len(nums)-1]+1, upper)
		return output


test = Solution()
print(test.findMissingRanges1([0,1,3,50,75], lower= 0, upper=99))

print(test.findMissingRanges1([-1], lower= -2, upper=-1))
print(test.findMissingRanges1([], lower= 1, upper=1))
print(test.findMissingRanges1([1000000000], lower= 0, upper=1000000000))
