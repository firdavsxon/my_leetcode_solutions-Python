"""
Problem Statement #
In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.

Example 1:

Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]
Example 2:

Input: [2, 1, 3, 2]
Output: [1, 3]
"""


class Solution:

	def find_single_numbers(self, nums):
		n1xn2 = 0
		for num in nums:
			n1xn2 ^= num

		rightmost_set_bit =1
		while (rightmost_set_bit & n1xn2) == 0:
			rightmost_set_bit = rightmost_set_bit << 1
		num1, num2 = 0, 0

		for num in nums:
			if (num & rightmost_set_bit) != 0:  # the bit is set
				num1 ^= num
			else:
				num2 ^= num
		return num1, num2




test = Solution()

array = [3, 3, 4, 1, 5, 5, 6, 6]

print(test.find_single_numbers(array))