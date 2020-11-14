"""
The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output:

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

    def hammingDistance1(self, x: int, y: int)-> int:
        mask = x ^ y
        out = 0
        while mask:
            if mask%2:
                out += 1
            mask //= 2
        return out

	
test = Solution()
print(test.hammingDistance1(1, 4))
