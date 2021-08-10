class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        N=len(cost)
        dp = [None] * N
        dp[N-1] = cost[N-1]
        dp[N-2] = cost[N-2]
        for i in range(N-3,-1,-1):
            dp[i] = min(cost[i]+dp[N-1],cost[i]+dp[N-2])
        return dp[0]

model = Solution()
model.minCostClimbingStairs([10,15,20])