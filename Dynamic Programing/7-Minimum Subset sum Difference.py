"""

Partition a set into two subsets such that the difference of subset sums is minimum

Given a set of integers, the task is to divide it into two sets S1 and S2 such that 
the absolute difference between their sums is minimum. 
If there is a set S with n elements, then if we assume Subset1 has m elements, 
Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) 
should be minimum.

Example: 

Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11

"""
# https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
import sys


def MinimumSubsetSumDifference(arr):
    m = len(arr)
    total = sum(arr)
    dp = [[0 for i in range(total + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        for j in range(total + 1):
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            elif arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    gg = dp[-1][: total // 2]
    minimum = sys.maxsize

    for i in range(len(gg) + 1):
        if dp[-1][i] == True:
            s2 = total - i
            minimum = min(minimum, abs(s2 - i))
    return minimum


print(MinimumSubsetSumDifference([1, 6, 11, 5]))
