"""

Remove Covered Intervals
Medium

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
 

Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li < ri <= 105
All the given intervals are unique.
Discussion | Solution

"""


# Let us sort our intervals by their starts and traverse them one
# by one (if we have the same ends, we first choose intervals
# with smaller ends, so they will be traversed first) Also let
# us keep right variable, which will be the biggest right end
# of interval so far. So, what does it mean that one interval
# is covered by some other? It means that end <= right: we have
# some previous interval with end more than current end and
# start which is less than current interval.

# Complexity: for time complexity we sort intervals in O(n log n) and then traverse them in O(n). Space complexity is O(n) if we are not allowed to change intervals and O(log n) we are allowed to modify intervals.
from typing import List


# https: // www.youtube.com/watch?v = nhAsMabiVkM & ab_channel = NeetCode


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i: (i[0], -i[1]))
        farthest = 0
        covered = 0
        for i in range(len(intervals)):
            start, end = intervals[i]
            if end > farthest:
                farthest = end
            else:
                covered += 1

        return len(intervals) - covered
