"""
Date: - 29/07/21

Source :- https://leetcode.com/problems/last-stone-weight/

1046. Last Stone Weight
Easy

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  
Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y 
has new weight y-x.

At the end, there is at most 1 stone left.  
Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000

"""

# Solution from where i learnt
# https://www.youtube.com/watch?v=B-QCq79-Vfw&ab_channel=NeetCode

# Since python doesnt have a max heap inbuilt so we will be using min heap and modify our elements

from heapq import heapify, heappush, heappop


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> (int, int):

        # Preprocessing of the list in order to use min heap
        stones = [-s for s in stones]

        # Heapify the stones list
        heapify(stones)

        while len(stones) > 1:
            first = heappop(stones)
            second = heappop(stones)
            if first != second:
                heappush(stones, -(-first - -second))

        stones.append(0)
        return abs(stones[0])
