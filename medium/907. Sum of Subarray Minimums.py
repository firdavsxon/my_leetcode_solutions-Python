"""
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.



Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444

"""
from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr = [0] + arr
        result = [0]* len(arr)
        stack = [0]

        for idx, current_number in enumerate(arr):
            while arr[stack[-1]]> current_number:
                stack.pop()
            prev_idx = stack[-1]
            result[idx] = result[prev_idx] + current_number*(idx - prev_idx)
            stack.append(idx)
        return sum(result)%(10**9+7)



test = Solution()
array=[3,1,2,4]
print(test.sumSubarrayMins(array))