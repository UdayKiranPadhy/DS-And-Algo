"""
Subset Sum Problem |

Given a set of non-negative integers, and a value sum, determine if there is a subset
of the given set with sum equal to given sum. 

Example: 

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""

# Recursive method
def SubsetSum(array, n, sum):
    if sum == 0:
        return True
    elif n == 0 and sum != 0:
        return False
    elif array[n] <= sum:
        return SubsetSum(array, n - 1, sum - array[n]) or SubsetSum(array, n - 1, sum)
    else:
        return SubsetSum(array, n - 1, sum)


print(SubsetSum([3, 34, 4, 12, 5, 2], 5, 9))  # True
print(SubsetSum([3, 34, 4, 12, 5, 2], 5, 30))  # False


# Memorization Method Bottom to top method
def SubsetSum2(array, n, sum):
    global dp
    if dp[n][sum] == False or dp[n][sum] == True:
        return dp[n][sum]
    else:
        if sum == 0:
            dp[n][sum] = True
            return True
        elif n == 0 and sum != 0:
            dp[n][sum] = False
            return False
        elif array[n] <= sum:
            dp[n][sum] = SubsetSum(array, n - 1, sum - array[n]) or SubsetSum(
                array, n - 1, sum
            )
            return dp[n][sum]
        else:
            dp[n][sum] = SubsetSum(array, n - 1, sum)
            return dp[n][sum]


array = [3, 34, 4, 12, 5, 2]
n = len(array)
sum = 9
dp = [[None for i in range(sum + 1)] for i in range(n + 1)]
print(SubsetSum2([3, 34, 4, 12, 5, 2], 5, 9))  # True


sum = 30
dp = [[None for i in range(sum + 1)] for i in range(n + 1)]
print(SubsetSum2([3, 34, 4, 12, 5, 2], 5, 30))  # False


import sys

sys.setrecursionlimit(10**9)

# Top-Down Approach
def SubsetSum3(array, sum):
    m = len(array)
    dp = [[0 for i in range(sum + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(sum + 1):
            if j == 0:
                dp[i][j] = True
            elif i == 0 and j != 0:
                dp[i][j] = False
            elif array[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - array[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


print(SubsetSum3([3, 34, 4, 12, 5, 2], 9))
print(SubsetSum3([3, 34, 4, 12, 5, 2], 30))
