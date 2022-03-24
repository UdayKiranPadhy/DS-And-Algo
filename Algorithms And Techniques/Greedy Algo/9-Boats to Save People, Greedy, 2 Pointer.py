"""

881. Boats to Save People
Medium

You are given an array people where people[i] is the weight of the ith person, 
and an infinite number of boats where each boat can carry a maximum weight of 
limit. Each boat carries at most two people at the same time, provided the 
sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 

Constraints:

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104

"""


# https://leetcode.com/problems/boats-to-save-people

# The key intuition here is that:

# Every person must be saved.
# For each person it is better to find another person with biggest weight, such 
# that sum of their weights is no more than limit. Indeed, if we put another 
# person, we will have subproblem A, which is always worse than if we put 
# biggest one (subproblem B): every solution of B can be also used to solve 
# A as well, but not the opposite.
# So, let us sort our people by weight and use two pointers technique to allocate 
# them to boats:

# If people[beg] + people[end] <= limit, then we can put these two persons in one 
# boat, so we move beg to the right, end to the left and increment ans by one.
# In opposite case it means, that person with smallest weight and with biggest 
# weight so far can not be put in one boat, so, we need to decrease weight: movint 
# end pointer one step to the left.
# Complexity: time complexity is O(n log n), because we sorted our data and then 
# we have O(n) for two-pointers approach. Space complexity is O(n).

from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        ans = 0
        while (i <= j):
            ans += 1
            if people[i] + people[j] <= limit:
                i+= 1
            j-=1
        return ans