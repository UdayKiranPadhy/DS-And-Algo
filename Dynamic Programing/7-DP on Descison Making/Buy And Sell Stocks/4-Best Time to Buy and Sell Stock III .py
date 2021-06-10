"""
Problem Statement :- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
Date :- 10/6/21

123. Best Time to Buy and Sell Stock III
Hard

3722

91

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 10^5
0 <= prices[i] <= 10^5



"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        N = len(prices)

        def profit(index, own, transatations):
            if index == N or transatations == 0:
                return 0

            if own == 1:
                op1 = prices[index] + profit(index+1, 0, transatations-1)
                op2 = profit(index+1, own, transatations)
                return max(op1, op2)
            else:
                op1 = -prices[index] + profit(index+1, 1, transatations)
                op2 = profit(index+1, own, transatations)
                return max(op1, op2)

        if len(prices) < 2:
            return 0

        return profit(0, 0, 2)