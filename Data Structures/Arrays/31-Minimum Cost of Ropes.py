"""
Source :- Edyst
Date:- 21/06/2021

Minimum Cost of ropes

There are given N ropes of different lengths, we need to connect these ropes 
into one rope. The cost to connect two ropes is equal to sum of their lengths. 
The task is to connect the ropes with minimum cost.

Example Input:
4 3 2 6
Output:
29

Example Input:
4 2 7 6 9
Output:
62

Explanation:
For example if we are given 4 ropes of lengths 4, 3, 2 and 6. We can connect 
the ropes in following ways.
1) First connect ropes of lengths 2 and 3. Now we have three ropes of lengths 4, 6 and 5.
2) Now connect ropes of lengths 4 and 5. Now we have two ropes of lengths 6 and 9.
3) Finally connect the two ropes and all ropes have connected.

Total cost for connecting all ropes is 5 + 9 + 15 = 29. This is the optimized 
cost for connecting ropes. Other ways of connecting ropes would always have same or more cost.

"""
from collections import deque


class Solution:
    def minCost(self, A):
        solutions = []
        A.sort()
        d = deque(A)
        while len(d) != 1:
            a = d.popleft()
            b = d.popleft()
            cost = a+b
            d.appendleft(cost)
            solutions.append(cost)
            d = deque(sorted(d))
        print(sum(solutions))


model = Solution()
model.minCost([4, 2, 7, 6, 9])
