"""

1029. Two City Scheduling
Medium

2393

232

Add to List

Share
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

 

Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086
 

Constraints:

2 * n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000


"""


from functools import lru_cache
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)

        @lru_cache(None)
        def dp(index, cityA, cityB):
            if index == N and cityA == 0 and cityB == 0:
                return 0
            if cityA > 0 and cityB > 0:
                op1 = costs[index][0] + dp(index+1, cityA-1, cityB)
                op2 = costs[index][1] + dp(index+1, cityA, cityB-1)
                return min(op1, op2)
            elif cityB > 0:
                op1 = costs[index][1] + dp(index+1, cityA, cityB-1)
                return op1
            else:
                op1 = costs[index][0] + dp(index+1, cityA-1, cityB)
                return op1

        return dp(0, N//2, N//2)
