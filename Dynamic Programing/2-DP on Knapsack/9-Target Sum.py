"""

Target Sum

You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the 
symbols '+' and '-' before each integer in nums and then concatenate 
all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and 
a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, 
which evaluates to target.

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000

"""

# same as count of subset of given sum .


def TargetSum(array, target):
    n = len(array)
    s1 = (target + sum(array)) // 2
    dp = [[0 for i in range(s1 + 1)] for j in range(n + 1)]

    for i in range(n + 1):
        for j in range(s1 + 1):
            if j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = 0
            elif array[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - array[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


nums = [1, 1, 1, 1, 1]
target = 3
print(TargetSum(nums, target))
