"""
Problem Statement :-https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
Date :- 10/6/21

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you 
like (i.e., buy one and sell one share of the stock multiple times) with the following 
restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell 
the stock before you buy again).
 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000


"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        N = len(prices)

        def profit(index, own, cooldown):
            if index >= N:
                return 0
            if (own==1):
                op1 = prices[index] + profit(index+1, 0, 1)
                op2 = profit(index+1, 1, 0)
                return max(op1, op2)
            else:
                if cooldown==1:
                    op1 = profit(index+1, 0, 0)
                else:
                    op1 = -prices[index] + profit(index+1, 1, 0)
                op2 = profit(index+1,own,cooldown)
                return max(op1,op2)
        return profit(0,0,0)
