"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        for i in range(numRows):
            temp = [None for _ in range(i+1)]
            temp[0], temp[-1] = 1, 1
            j=1
            while j<len(temp)-1:
                temp[j] = out[i-1][j-1] + out[i-1][j]
                j+=1
            out.append(temp)
        return out

test = Solution()
print(test.generate(5))
