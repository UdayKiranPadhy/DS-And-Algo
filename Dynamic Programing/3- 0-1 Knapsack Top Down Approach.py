"""
0-1 Knapsack Problem |
Given weights and values of n items, put these items in a knapsack of capacity W 
to get the maximum total value in the knapsack. In other words, given two integer 
arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated 
with n items respectively. Also given an integer W which represents knapsack capacity, 
find out the maximum value subset of val[] such that sum of the weights of this subset 
is smaller than or equal to W. You cannot break an item, either pick the complete item 
or don’t pick it (0-1 property).
"""


def Knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weights[i - 1] <= j:
                dp[i][j] = max(
                    values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j]
                )
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]


print(Knapsack([1, 2, 3], [10, 15, 40], 6))
