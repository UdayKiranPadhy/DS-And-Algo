# Question
"""

Given a set of elements, we are required to find the number of ways 
in which we can divide the set into 2 subsets so that the difference 
of their sum value is equal to the given difference.

"""

# Solution
"""
SumOfSubset1 - SumOfSubset2 = GivenDifference ----------(1)

SumOfSubset1 + SumOfSubset2 = SumOfElements    -----------(2)

(1) + (2) =>

2SumOfSubset1 = GivenDifference + SumOfElements

SumOfSubset = (GivenDifference+ SumOfElements) / 2 

So we need to count the subsets whose 
sum is equal to (GivenDifference+ SumOfElements) / 2 

"""


def Subsets(array, difference):
    capacity = (sum(array) + difference) // 2
    m = len(array)

    dp = [[0 for i in range(capacity + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(capacity + 1):
            if j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 0
            elif array[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - array[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


print(Subsets([3, 1, 2, 3], 3))
