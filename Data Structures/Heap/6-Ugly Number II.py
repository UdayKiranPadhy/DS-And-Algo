"""

264. Ugly Number II
Medium

https://leetcode.com/problems/ugly-number-ii/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
 

Constraints:

1 <= n <= 1690

"""

from heapq import heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        pq = [1]
        seen = set([1])

        while len(pq):
            popedElement = heappop(pq)
            n -= 1
            if n == 0:
                return popedElement
            if popedElement*2 not in seen:
                seen.add(popedElement*2)
                heappush(pq, popedElement*2)
            if popedElement*3 not in seen:
                seen.add(popedElement*3)
                heappush(pq, popedElement*3)
            if popedElement*5 not in seen:
                seen.add(popedElement*5)
                heappush(pq, popedElement*5)


# https://www.youtube.com/watch?v=X5SuOsIWCoI&ab_channel=probability_coding_is_fun_is_1
#
# Let us solve this problem for general case: that is not only for 2,3,5 divisors,
# but for any of them and any number of them. factors = [2,3,5] and k=3 in our case.
# Let Numbers be an array, where we keep all our ugly numbers. Also, note, that any
# ugly number is some other ugly number, multiplied by 2, 3 or 5. So, let starts be
# the indexes of ugly numbers, that when multiplied by 2, 3 or 5 respectively, produces
# the smallest ugly number that is larger than the current overall maximum ugly number..
# Let us do several first steps to understand it better:

# starts = [0,0,0] for numbers 2,3,5, so new_num = min(1*2,1*3,1*5) = 2, and now starts = [1,0,0], Numbers = [1,2].
# starts = [1,0,0], so new_num = min(2*2,1*3,1*5) = 3, and now starts = [1,1,0], Numbers = [1,2,3].
# starts = [1,1,0], so new_num = min(2*2,2*3,1*5) = 4, so now starts = [2,1,0], Numbers = [1,2,3,4].
# starts = [2,1,0], so new_num = min(3*2,2*3,1*5) = 5, so now starts = [2,1,1], Numbers = [1,2,3,4,5].
# starts = [2,1,1], so new_num = min(3*2,2*3,2*5) = 6, so let us be carefull in this case: we need to increase two numbers from start, because our new number 6 can be divided both by 2 and 3, so now starts = [3,2,1], Numbers = [1,2,3,4,5,6].
# starts = [3,2,1], so new_num = min(4*2,3*3,2*5) = 8, so now starts = [4,2,1], Numbers = [1,2,3,4,5,6,8]
# starts = [4,2,1], so new_num = min(5*2,3*3,2*5) = 9, so now starts = [4,3,1], Numbers = [1,2,3,4,5,6,8,9].
# starts = [4,3,1], so new_num = min(5*2,4*3,2*5) = 10, so we need to update two elements from starts and now starts = [5,3,2], Numbers = [1,2,3,4,5,6,8,9,10]
# starts = [5,3,2], so new_num = min(6*2,4*3,3*5) = 12, we again need to update two elements from starts, and now starts = [6,4,2], Numbers = [1,2,3,4,5,6,8,9,10,12].
# starts = [6,4,2], so new_num = min(8*2,5*3,3*5) = 15, we again need to update two elements from starts, and now starts = [6,5,3], Numbers = [1,2,3,4,5,6,8,9,10,12,15].

# Complexity: time complexity is O(n) to find ugly number with number n, because on each step we check 3 possible candidates. Space complexity is O(n) as well. Note, that it can be easily generalized for different amount of divisors with time complexity O(nk), where k is total number of divisors.

class Solution:
    def nthUglyNumber(self, n):
        factors, k = [2, 3, 5], 3
        starts, Numbers = [0] * k, [1]
        for i in range(n-1):
            candidates = [factors[i]*Numbers[starts[i]] for i in range(k)]
            new_num = min(candidates)
            Numbers.append(new_num)
            starts = [starts[i] + (candidates[i] == new_num) for i in range(k)]
        return Numbers[-1]
