"""

Problem Statement  :- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

122. Best Time to Buy and Sell Stock II
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you 
like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions 
simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e., max profit = 0.
 
Example 4:

Input: prices = [3,3]
Output: 0
Explanation: In this case, no transaction is done, i.e., max profit = 0.

Example 5:

Input: prices = [1]
Output: 0
Explanation: In this case, no transaction is done, i.e., max profit = 0.


Constraints:

1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4

"""

# Solution , My Trails , Success

# Peak Valley Approach


def main():
    prices = [int(x) for x in input().split(" ")]
    N = len(prices)
    if N < 2:
        return 0
    buying_date = 0
    previous = prices[0]
    selling_date = 1
    next_buying_date = 0
    profit = 0
    while True:
        while prices[selling_date] >= previous:
            previous = prices[selling_date]
            selling_date += 1
            if selling_date == N:
                profit += (prices[selling_date-1]-prices[buying_date])
                return profit
        selling_date -= 1
        profit += (prices[selling_date] - prices[buying_date])
        next_buying_date = selling_date
        next_buying_date += 1
        while previous >= prices[next_buying_date]:
            previous = prices[next_buying_date]
            next_buying_date += 1
            if next_buying_date == N:
                return profit
        buying_date = next_buying_date - 1
        selling_date = next_buying_date


if __name__ == '__main__':
    print(main())


# Other Solutions

# Simple One Pass Approach
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += prices[i+1]-prices[i]

        return profit
