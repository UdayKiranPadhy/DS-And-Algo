"""

Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step
on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].


Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
   Hide Hint #1


Hint - 1
Say f[i] is the final cost to climb to the top from step i. Then
f[i] = cost[i] + min(f[i+1], f[i+2]).

"""


# Solution

#  Solution - I (Brute-Force)

# We just do what the problem asks us. We can start either at 0th or 1st step
# and after that we have the choice to either climb one step or two steps.

def minCostClimbingStairs(cost):
    return min(solve(cost, 0), solve(cost, 1))


def solve(cost, i):
    if(i >= len(cost)):
        return 0  # reached end - no more cost required
    # pay current cost and choose min(step+1, step+2) based on which takes us
#  to end with minimum cost
    return cost[i] + min(solve(cost, i + 1), solve(cost, i + 2))


# Time Complexity : O(2^N)
# Space Complexity : O(N)


#  Solution - II (Dynamic Programming - Memoization)

# The brute force solution leads to TLE because we are doing unnecessary
# re-calculations for the same steps multiple times. Instead, we can opt
# to store the calculated result for a given step and use it whenever required
# in the future instead of repeating the calculation.

# Here, I am using dp array where dp[i] will denote the minimum cost required to
# reach the end starting from the ith step. Each element of dp is initialised to 0
# at the start and once we calculate the minimum cost to reach from ith step to
# the end, we will store it in dp[i] and use it in the future calculation of
# previous steps.

def minCostClimbingStairs(cost):
    dp = [0]*len(cost)  # dp[i] = cost to reach end from ith step
    return min(solve(cost, dp, 0), solve(cost, dp, 1))


def solve(cost, dp, i):
    if(i >= len(cost)):
        return 0
    # if already calculated, directly return stored minimum cost
    if(dp[i]):
        return dp[i]
        # same as above, just store in dp[i] before returning
    dp[i] = cost[i] + min(solve(cost, dp, i + 1), solve(cost, dp, i + 2))
    return dp[i]

# Time Complexity : O(N), where N is the number of steps. We will only be calculating minimum cost for each step once instead of recomputing it over and over as in brute force.
# Space Complexity : O(N), required for maintaining dp array.


# Solution - III (Dynamic Programming - Tabulation)

# We can also solve this iteratively. Here, we will start storing results from the start
# and make our way till the end (bottom-up).

# Again, We have choice to start at 0th or 1st step. Then, for each of the next steps,
# we could reach there either from the previous step or previous-to-previous step.
# Here, we will be using dp array where dp[i] will denote the minimum cost required to
#  reach ith step starting from 0th or 1st step.Thus, we have the relation -
# dp[i] = cost[i] + min(dp[i - 1], dp[i - 2]). The cost[i] term won't be added in the
# nth step since we would already have reached the destination

def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0]*(n+1)
    dp[0] = cost[0]
    dp[1] = cost[1]
    for i in range(2, n+1):
        if i >= n:
            dp[i] = 0
        else:
            # we can reach here from i-1th or i-2th step - choose minimum
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return dp[n]

# Time Complexity: O(N)
# Space Complexity: O(N)

# Solution - IV (Dynamic Programming - Constant Space)

# We can observe that we are only ever accessing the previous or
# previous-to-previous step. So, in the iterative version, we don't really
# need to store the whole dp array and we can just store the minimum cost
# required to reach the i-1th and i-2th steps.


def minCostClimbingStairs(cost):
    # // just store minimum cost to reach i-1th and i-2th step instead of whole array
    n = len(cost)
    prev = cost[1]
    prev2 = cost[0]
    cur = min(prev, prev2)
    for i in range(2, n+1):
        if i == n:
            cur = 0 + min(prev, prev2), prev2 = prev, prev = cur
        else:
            cur = cost[i] + min(prev, prev2), prev2 = prev, prev = cur
        return cur

# Time Complexity : O(N)
# Space Complexity : O(1)
