"""

1986. Minimum Number of Work Sessions to Finish the Tasks
Medium

https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

There are n tasks assigned to you. The task times are represented as an integer array tasks of length n, where the ith task takes tasks[i] hours to finish. A work session is when you work for at most sessionTime consecutive hours and then take a break.

You should finish the given tasks in a way that satisfies the following conditions:

If you start a task in a work session, you must complete it in the same work session.
You can start a new task immediately after finishing the previous one.
You may complete the tasks in any order.
Given tasks and sessionTime, return the minimum number of work sessions needed to finish all the tasks following the conditions above.

The tests are generated such that sessionTime is greater than or equal to the maximum element in tasks[i].

 

Example 1:

Input: tasks = [1,2,3], sessionTime = 3
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
- Second work session: finish the third task in 3 hours.
Example 2:

Input: tasks = [3,1,3,1,1], sessionTime = 8
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish all the tasks except the last one in 3 + 1 + 3 + 1 = 8 hours.
- Second work session: finish the last task in 1 hour.
Example 3:

Input: tasks = [1,2,3,4,5], sessionTime = 15
Output: 1
Explanation: You can finish all the tasks in one work session.
 

Constraints:

n == tasks.length
1 <= n <= 14
1 <= tasks[i] <= 10
max(tasks[i]) <= sessionTime <= 15

"""
# Let dp(mask, remainTime) is the minimum of work sessions needed to finish all the
# tasks represent by mask (where ith bit = 1 means tasks[i] need to proceed) with
# the remainTime we have for the current session.
# Then dp((1 << n) - 1, 0) is our result
# We use mask as 111...1111, represent we need to process all n tasks.
# We pass remainTime = 0, which means there is no remain time for the current
# session; ask them to create a new session.


from functools import lru_cache
from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        def clearBit(x, k):
            return ~(1 << k) & x

        @lru_cache(None)
        def dp(mask, remainTime):
            if mask == 0:
                return 0

            ans = n  # There is up to N work sessions
            for i in range(n):
                if (mask >> i) & 1:
                    newMask = clearBit(mask, i)
                    if tasks[i] <= remainTime:
                        # Consume current session
                        ans = min(ans, dp(newMask, remainTime - tasks[i]))
                    else:
                        # Create new session
                        ans = min(ans, dp(newMask, sessionTime - tasks[i]) + 1)

            return ans

        return dp((1 << n) - 1, 0)


# Complexity:

# Time: O(2^n * sessionTime * n), where n <= 14 is length of tasks, sessionTime <= 15.
# Explain: There is total 2^n * sessionTime dp states, they are dp[0][0], dp[1][0]...,
# dp[2^n-1][remainTime]. Each dp state needs an inner loop O(n) to calculate the result.
# Space: O(2^n * sessionTime)
