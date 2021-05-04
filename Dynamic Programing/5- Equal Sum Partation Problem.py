"""
Partition problem |
Partition problem is to determine whether a given set can be partitioned into two 
subsets such that the sum of elements in both subsets is the same. 

Examples: 

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.
"""

# Just same problem as Subset sum problem, we need to find a subset of sum equal to total sum of the array.
def SubsetSum(array, sum):
    m = len(array)
    dp = [[0 for i in range(sum + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(sum + 1):
            if sum == 0:
                dp[i][j] = True
            elif i == 0 and sum != 0:
                dp[i][j] = False
            elif array[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - array[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


def EqualSumPartition(array):
    if sum(array) % 2 != 0:
        return False
    else:
        return SubsetSum(array, sum(array) % 2)


print(EqualSumPartition([1, 5, 11, 5]))
