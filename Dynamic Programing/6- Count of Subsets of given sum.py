"""

Count of subsets with sum equal to X
Given an array arr[] of length N and an integer X, the task is to find the number of 
subsets with sum equal to X.

Examples: 

Input: arr[] = {1, 2, 3, 3}, X = 6 
Output: 3 
All the possible subsets are {1, 2, 3}, 
{1, 2, 3} and {3, 3}
 

Input: arr[] = {1, 1, 1, 1}, X = 1 
Output: 4 

"""

# Recursive Approach


def CountSubsets(arr, sum, n):
    if sum < 0:
        return 0
    if sum == 0:
        return 1
    elif n == 0 and sum != 0:
        return 0
    elif arr[n - 1] <= sum:
        return CountSubsets(arr, sum - arr[n - 1], n - 1) + CountSubsets(
            arr, sum, n - 1
        )
    else:
        return CountSubsets(arr, sum, n - 1)


print(CountSubsets([1, 2, 3, 6, 5], 6, 5))
print(CountSubsets([1, 2, 3, 3], 6, 4))


# Top Down Approach


def CountSubsets2(arr, sum):
    m = len(arr)
    dp = [[0 for i in range(sum + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(sum + 1):
            if j == 0:
                dp[i][j] = 1
            elif i == 0 and j != 0:
                dp[i][j] = 0
            elif arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


print(CountSubsets2([1, 2, 3, 6, 5], 6))
