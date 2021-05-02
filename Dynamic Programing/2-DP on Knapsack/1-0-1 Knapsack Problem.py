"""
There are mainly divided into 6 sub similar problems which after learing u can do any 7th 
sub problems 
They are 
1-Subset sum
2-Equal sum partation 
3-Count of subset sum
4-Minium subset sum difference
5-Target sum
6-Hash of subset e give differnce
"""
# Usually Dp starts leaning from knapsack
# knapsack is basically 3 types
# fractional knapsack(greedy algo)
# 0-1 knapsack
# and unbounded knapsack

# knapsack is a bag
"""
0-1 Knapsack Problem 
Given weights and values of n items, put these items in a knapsack of capacity 
W to get the maximum total value in the knapsack. In other words, given two 
integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights 
associated with n items respectively. Also given an integer W which represents 
knapsack capacity, find out the maximum value subset of val[] such that sum of 
the weights of this subset is smaller than or equal to W. You cannot break an 
item, either pick the complete item or don’t pick it (0-1 property).
"""

