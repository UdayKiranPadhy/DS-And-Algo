"""

Problem Statement :-https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
Date:- 09-06-2021

714. Best Time to Buy and Sell Stock with Transaction Fee
Medium

You are given an array prices where prices[i] is the price of a given stock on 
the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions 
as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you 
must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 

Constraints:

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104


"""

from functools import lru_cache


class Solution:

    def maxProfit(self, prices: list[int], fee: int) -> int:
        N = len(prices)

        @lru_cache(None)
        def profit(index, own, fee):
            if index >= N:
                return 0
            if (own == 1):
                op1 = prices[index] + profit(index+1, 0, fee)
                op2 = profit(index+1, 1, fee)
                return max(op1, op2)
            else:
                op1 = -(prices[index] + fee) + profit(index+1, 1, fee)
                op2 = profit(index+1, 0, fee)
                return max(op1, op2)

        return profit(0, 0, fee)
