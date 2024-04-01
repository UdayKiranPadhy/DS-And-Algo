"""

787. Cheapest Flights Within K Stops
Medium

There are n cities connected by some number of flights. You are given an array flights
where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city
from i to city toi with cost price i.

You are also given three integers src, dst, and k, return the cheapest price from src
to dst with at most k stops. If there is no such route, return -1.


Example 1:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation: The graph is shown.
The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
 

Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst

"""


# https://leetcode.com/problems/cheapest-flights-within-k-stops

# Solution 1
# Appling Bellman Ford Algo k+1 times , For more info read the 23-Bellman Ford pdf go listen to
# gate Smahers video on youtube
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')]*n
        prices[src] = 0

        for _ in range(k+1):
            temp = prices.copy()
            for u, v, cost in flights:
                if prices[u] == float('inf'):
                    continue
                else:
                    if prices[u] + cost < temp[v]:
                        temp[v] = prices[u] + cost
            prices = temp
        return -1 if prices[dst] == float('inf') else prices[dst]


# There are a lot of different ways to handle this problem: using DFS, BFS, Dijkstra, Bellman-Ford,
# Dynamic programming. For me it is easier to use BFS, because we are asked to find the
# shortest distance between two given cities, not with all dst like in Dijkstra or Bellman-Ford.

# BFS the idea is to traverse our graph in usual bfs routine and also take into account that we
# can have maximum k stops, that is our pathes should have length less or equal than k + 1. To
# implement bfs in python usual way is to use deque (double ended queue), it works pretty fast
# in python. We can not use usual list like in dfs (for similate stack), because here we need
# to pop elements from the beginning of our queue.

# We need to keep in each cell of our queue 3 values: current city, current number of visited
# cities and current price. It is worth to investigate new city if 3 conditions met:

# Our current price is less or equal to minumum price found so far.
# If we still can visit one more city, visited < k+1.
# The current city is not our destination yet.
# If we reached our city of destination, we update minimum price we get so far.

# Complexity, both time and memory of bfs is O(V + E), where E is number of edges and V is
# number of vertices. Note however, that we have here multipass bfs, when we visit node,
# we do not mark it as visited, and we can visit it several times. In fact this algorighm
# is very similar to Dijkstra algorighm, and I think complexity is O(E + V^2) = E(V^2),
# because we traverse each edge only once, but we can visit nodes a lot of times. Update
# I do no think it is quite true, need to be checked.
