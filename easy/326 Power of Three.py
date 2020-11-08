"""
Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == x3.



Example 1:

Input: n = 27
Output: true
Example 2:

Input: n = 0
Output: false
Example 3:

Input: n = 9
Output: true
Example 4:

Input: n = 45
Output: false
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n%3 == 0:
            n/=3
        return n==1


test =Solution()
print(test.isPowerOfThree(27))
print(test.isPowerOfThree(9))