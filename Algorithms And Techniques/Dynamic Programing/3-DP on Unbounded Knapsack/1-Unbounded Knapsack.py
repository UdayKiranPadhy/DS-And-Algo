"""
Unbounded Knapsack (Repetition of items allowed)

Given a knapsack weight W and a set of n items with certain value 
val[i] and weight wt[i], we need to calculate the maximum amount 
that could make up this quantity exactly. This is different from 
classical Knapsack problem, here we are allowed to use unlimited 
number of instances of an item.

Examples: 

Input : W = 100
       val[]  = {1, 30}
       wt[] = {1, 50}
Output : 100
There are many ways to fill knapsack.
1) 2 instances of 50 unit weight item.
2) 100 instances of 1 unit weight item.
3) 1 instance of 50 unit weight item and 50
   instances of 1 unit weight items.
We get maximum value with option 2.

Input : W = 8
       val[] = {10, 40, 50, 70}
       wt[]  = {1, 3, 4, 5}       
Output : 110 
We get maximum value with one unit of
weight 5 and one unit of weight 3.

"""

# Recursive Approach
def UnboundedKnapSack(wt, val, n, capacity):
    if n == 0 or capacity <= 0:
        return 0
    elif wt[n - 1] <= capacity:
        return max(
            val[n - 1] + UnboundedKnapSack(wt, val, n, capacity - wt[n - 1]),
            UnboundedKnapSack(wt, val, n - 1, capacity),
        )
    else:
        return UnboundedKnapSack(wt, val, n - 1, capacity)


# print(UnboundedKnapSack([1, 50], [1, 30], 2, 100))

# Memorizatation Bottom top approach
def UnboundedKnapSack2(wt, val, n, capacity):
    global dp
    if dp[n][capacity] != -1:
        return dp[n][capacity]
    else:
        if n == 0 or capacity <= 0:
            dp[n][capacity] = 0
            return dp[n][capacity]
        elif wt[n - 1] <= capacity:
            dp[n][capacity] = max(
                val[n - 1] + UnboundedKnapSack(wt, val, n, capacity - wt[n - 1]),
                UnboundedKnapSack(wt, val, n - 1, capacity),
            )
            return dp[n][capacity]
        else:
            dp[n][capacity] = UnboundedKnapSack(wt, val, n - 1, capacity)
            return dp[n][capacity]


weight = [1, 3, 4, 5]
values = [10, 40, 50, 70]
capacity = 8
dp = [[-1 for i in range(capacity + 1)] for j in range(len(weight) + 1)]
print(UnboundedKnapSack2(weight, values, len(weight), capacity))


def UnboundedKnapSack3(wt, val, capacity):
    n = len(wt)
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]
    for i in range(n + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif j >= wt[i - 1]:
                dp[i][j] = max(val[i - 1] + dp[i][j - wt[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


print(UnboundedKnapSack3([1, 3, 4, 5], [10, 40, 50, 70], 8))
