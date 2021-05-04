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

# Memorization Approch
def Knapsack(weight, values, W, n):
    global dp
    if dp[W][n]:
        return dp[W][n]
    else:
        if W <= 0 or n == 0:
            if W < 0:
                dp[0][n] = 0
            else:
                dp[W][n] = 0
            return 0
        elif weight[n - 1] <= W:
            dp[W][n] = max(
                Knapsack(weight, values, W, n - 1),
                values[n - 1] + Knapsack(weight, values, W - weight[n - 1], n - 1),
            )
            return dp[W][n]
        else:
            dp[W][n] = Knapsack(weight, values, W - weight[n - 1], n - 1)
            return dp[W][n]


val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
dp = [[-1 for i in range(n + 1)] for j in range(W + 1)]
print(Knapsack(wt, val, W, n))
# 220
