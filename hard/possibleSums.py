"""
You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. You want to know how many distinct sums you can make from non-empty groupings of these coins.

Example

For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should be
possibleSums(coins, quantity) = 9.

Here are all the possible sums:

50 = 50;
10 + 50 = 60;
50 + 100 = 150;
10 + 50 + 100 = 160;
50 + 50 = 100;
10 + 50 + 50 = 110;
50 + 50 + 100 = 200;
10 + 50 + 50 + 100 = 210;
10 = 10;
100 = 100;
10 + 100 = 110.
As you can see, there are 9 distinct sums that can be created from non-empty groupings of your coins.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer coins

An array containing the values of the coins in your collection.

Guaranteed constraints:
1 ≤ coins.length ≤ 20,
1 ≤ coins[i] ≤ 104.

[input] array.integer quantity

An array containing the quantity of each type of coin in your collection. quantity[i] indicates the number of coins that have a value of coins[i].

Guaranteed constraints:
quantity.length = coins.length,
1 ≤ quantity[i] ≤ 105,
(quantity[0] + 1) * (quantity[1] + 1) * ... * (quantity[quantity.length - 1] + 1) <= 106.

[output] integer

The number of different possible sums that can be created from non-empty groupings of your coins.
"""


def possibleSums(coins, quantity):
	maximum = sum((map(lambda t: t[0]*t[1], zip(coins, quantity))))

	dp = [False] * (maximum+1)
	dp[0] =True
	for coin, q in zip(coins, quantity):
		for b in range(coin):
			num = -1
			for i in range(b, maximum+1, coin):
				if dp[i]:
					num=0
				elif num>=0:
					num += 1
				dp[i] = 0 <= num <= q
	return sum(dp)-1


def possibleSums1(coins, quantity):
	possible_sums = {0}
	for c, q in zip(coins, quantity):
		possible_sums = {x + c * i for x in possible_sums for i in range(q + 1)}

	return len(possible_sums) - 1



print(possibleSums1(coins = [10, 50, 100], quantity = [1, 2, 1]))


""" 
Input:
coins: [10, 50, 100]
quantity: [1, 2, 1]
Expected Output:
9
"""