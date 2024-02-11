"""

# https://practice.geeksforgeeks.org/problems/circular-tour/1#
Circular tour
Medium Accuracy: 33.91% Submissions: 53434 Points: 4
Suppose there is a circle. There are N petrol pumps on that circle. You will be given two sets of data.
1. The amount of petrol that every petrol pump has.
2. Distance from that petrol pump to the next petrol pump.
Find a starting point where the truck can start to get through the complete circle without exhausting its petrol in between.
Note :  Assume for 1 litre petrol, the truck can go 1 unit of distance.

Example 1:

Input:
N = 4
Petrol = 4 6 7 4
Distance = 6 5 3 5
Output: 1
Explanation: There are 4 petrol pumps with
amount of petrol and distance to next
petrol pump value pairs as {4, 6}, {6, 5},
{7, 3} and {4, 5}. The first point from
where truck can make a circular tour is
2nd petrol pump. Output in this case is 1
(index of 2nd petrol pump).
Your Task:
Your task is to complete the function tour() which takes the required data as inputs and returns an integer denoting a point from where a truck will be able to complete the circle (The truck will stop at each petrol pump and it has infinite capacity). If there exists multiple such starting points, then the function must return the first one out of those. (return -1 otherwise)

Expected Time Complexity: O(N)
Expected Auxiliary Space : O(N)

Constraints:
2 ≤ N ≤ 10000
1 ≤ petrol, distance ≤ 1000



Company Tags
 Amazon FactSet Microsoft Morgan Stanley Zoho
Topic Tags
 Queue Two-pointer-algorithm

"""
from typing import List


# Optimal Approach
# Keep two variables named surplus and difficiet and if surplus becomes less than zero increment to difficiet , increment start to i, make sum to zero.
# https://youtu.be/nTKdYm_5-ZY
# https://youtu.be/nTKdYm_5-ZY?t=514


def tour(lis, n):
    fuels=[lis[i][0] for i in range(n)]
    distance=[lis[i][1] for i in range(n)]
    start = 0
    diff = 0
    sum = 0
    for i in range(n):
        sum = sum + fuels[i] - distance[i]
        if sum < 0:
            start = i + 1
            diff += sum
            sum = 0
    if sum + diff >= 0:
        return start 
    else:
        return -1



"""

Same Question on Leetcode :- https://leetcode.com/problems/gas-station/

134. Gas Station
Medium

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

 

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
 

Constraints:

n == gas.length == cost.length
1 <= n <= 105
0 <= gas[i], cost[i] <= 104


"""


# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:


nums = [1,2,3,4]

print(*nums)