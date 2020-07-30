"""
Say you have an array for which the ith element is
the price of a given stock on day i.

If you were only permitted to complete at most
one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length=len(prices)
        if prices is None or length == 0:
            return 0
        if length == 1:
            return 0
        max_num = 0
        i = 0
        while i < length - 1:
            j = i + 1
            temp = max(prices[j:]) - prices[i]
            if temp> max_num:
                max_num=temp
            i += 1
        if max_num > 0:
            return max_num
        return 0

    def maxProfit1(self, prices: List[int]) -> int:

        if prices == []:
            return 0

        pointer = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if max_profit < prices[i] - pointer:
                max_profit = prices[i] - pointer

            if prices[i] < pointer:
                pointer = prices[i]

        return max_profit


test = Solution()
print(test.maxProfit([7,6,4,3,2,1]))
print(test.maxProfit([1,2]))
print(test.maxProfit([7,1,3,4,5,6,2]))
print(test.maxProfit([1]))
print(test.maxProfit([]))
print(test.maxProfit([2,4,1]))
print(50*'*')
print(test.maxProfit1([7,6,4,3,2,1]))
print(test.maxProfit1([1,2]))
print(test.maxProfit1([7,1,3,4,5,6,2]))
print(test.maxProfit1([1]))
print(test.maxProfit1([]))
print(test.maxProfit1([2,4,1]))