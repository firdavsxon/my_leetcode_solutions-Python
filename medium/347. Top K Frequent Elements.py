"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
from heapq import *
from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        buckets = []
        flat_list = []
        for _ in range(len(nums)+1):
            buckets.append([])

        for number, frequent in count.items():
            buckets[frequent] = [number]
        for sublist in buckets:
            for i in sublist:
                flat_list.append(i)
        return flat_list[::-1][:k]
    def topKfrequent_with_heap(self, nums: List[int], k:int) -> List[int]:
        h = []
        count = Counter(nums)
        for key, val in count.items():
            heappush(h, (val, key))
            if len(h)>k:
                heappop(h)

        return [s for (i, s) in h]


test =Solution()
array = [1, 1 , 1, 2, 2 ,3]
k = 2
print(test.topKFrequent(array, k))
print(test.topKfrequent_with_heap(array, k))



