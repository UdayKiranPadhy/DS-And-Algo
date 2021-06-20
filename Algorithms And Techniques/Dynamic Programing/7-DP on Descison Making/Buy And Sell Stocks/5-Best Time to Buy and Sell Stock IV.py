"""

Problem Statement :- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
Date:- 10/6/21


188. Best Time to Buy and Sell Stock IV
Hard

You are given an integer array prices where prices[i] is the price of a given 
stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you 
must sell the stock before you buy again).


Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. 
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000

"""



from functools import lru_cache

class Solution:
    def maxProfit(self,k:int, prices: list[int]) -> int:
        N= len(prices)

        
        @lru_cache(None)
        def profit(index,own,transatations):
            if index == N or transatations ==0:
                return 0
            
            if own==1:
                op1 = prices[index] + profit(index+1,0,transatations-1)
                op2 = profit(index+1,own,transatations)
                return max(op1,op2)
            else:
                op1 = -prices[index] + profit(index+1,1,transatations)
                op2 = profit(index+1,own,transatations)
                return max(op1,op2)
                
        
        
        if len(prices) < 2:
            return 0
        
        return profit(0,0,k)