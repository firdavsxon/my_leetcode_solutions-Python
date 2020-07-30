"""
Say you have an array prices for which the ith element is
the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete
as many transactions as you like (i.e., buy one and sell one s
hare of the stock multiple times).

Note: You may not engage in multiple transactions at the same
time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


Constraints:

1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4

"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == []:
            return 0

        pointer = prices[0]
        max_profit = 0
        profits = []
        for i in range(len(prices)):
            if max_profit < prices[i] - pointer:
                max_profit = prices[i] - pointer
                profits.append(max_profit)
                pointer = prices[i]
                max_profit = 0

            if prices[i] < pointer:
                pointer = prices[i]

        return sum(profits)

    def maxProfit1(self, prices:List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += (prices[i] - prices[i - 1])
        return max_profit



test = Solution()
print(test.maxProfit([7,6,4,3,2,1]))
print(test.maxProfit([7,1,5,3,6,4,5,3,8]))
print(test.maxProfit1([7,1,5,3,6,4,5,3,8]))
