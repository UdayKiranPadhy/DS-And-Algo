"""

871. Minimum Number of Refueling Stops
Hard

2062

41

Add to List

Share
A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.

 

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can not reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.
 

Constraints:

1 <= target, startFuel <= 10^9
0 <= stations.length <= 500
0 <= positioni <= positioni+1 < target
1 <= fueli < 10^9

"""

# https://leetcode.com/problems/minimum-number-of-refueling-stops/
# https://www.youtube.com/watch?v=sKjKLN5JswQ&ab_channel=probability_coding_is_fun_is_1
from heapq import *
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        max_you_can_reach = startFuel
        stations.sort()
        index = 0
        stops = 0
        while max_you_can_reach < target:

            while index < len(stations) and stations[index][0] <= max_you_can_reach:
                heappush(pq, -stations[index][1])
                index += 1
            if len(pq) == 0:
                return -1
            max_you_can_reach += -pq[0]
            heappop(pq)
            stops += 1
        return stops
