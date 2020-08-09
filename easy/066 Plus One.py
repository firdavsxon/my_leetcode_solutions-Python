"""
Given a non-empty array of digits representing
a non-negative integer, increment one to the integer.

The digits are stored such that the most significant
 digit is at the head of the list, and each element
 in the array contains a single digit.

You may assume the integer does not contain any
leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
from typing import  List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d_str = ''
        for i in digits:
            d_str += str(i)
        d_int  = int(d_str)
        d_int += 1
        d_str = str(d_int)
        return [int(i) for i in d_str]

test = Solution()
print(test.plusOne([1,2,3,4]))
print(test.plusOne([9]))
print(test.plusOne([999]))