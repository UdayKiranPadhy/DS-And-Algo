"""

56. Merge Intervals
Medium

Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping 
intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4

"""
# Problem Statement
# https://leetcode.com/problems/merge-intervals

# Let us sort our intervals by its starts and then iterate them one by one: we 
# can have two options:

# The current ending point in our ans is less than beg of new interval: it means that 
# we have a gap and we need to add new interval to our answer.
# In the opposite case our intervals are overlapping, so we need to update the end 
# for last interval we created.

# Complexity: time complexity is O(n log n) to sort intervals and space complexity is 
# O(n) to keep sorted intervals and answer.

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ans = []
        for beg,end in sorted(intervals):
            if not ans or ans[-1][1] < beg:
                ans.append([beg,end])
            else:
                ans[-1][1] = max(ans[-1][1],end)
        return ans