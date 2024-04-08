"""
https://leetcode.com/problems/partition-labels/

763. Partition Labels
Medium

5476

227

Add to List

Share
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.

Tags := HashTable , 2 Pointer , String , Greedy

"""

# Problem Statement
# https://leetcode.com/problems/partition-labels

# Solution
# The idea of this solution is greedily construct our partition,
# let us consider the example S = ababcbacde fegdehijhklij. We need to
# start with letter a and we can not stop, until we reach the last
# occurrence of a: so, we need to take ababcba part at least. But if we
# take this part, we need to consider letters b and c as well and also
# traverse our string until we meet the last occurrence of these letters,
# so we need to take ababcbac. Here we can stop, because we already take
# into account all symbols inside this string. So, we go to the next symbol
# and repeat our partition. So, what we have in my code:

# First, we need to know all ends for each letter in advance, I call it ends.
# Also, curr is current index and last is index we need to traverse until.
# For each group of symbols we need to do: last = ends[S[curr]]: we find the
# place we need to traverse; while we do no reach this place, we look at the
# next symbol and update our last. So, we stop, when curr become greater than last.
# We add curr to our out result.
# Note, that we need to have [8, 7, 8] for our example, but we get [8, 15, 23],
# places where our partitions are. So, we evaluate differences 8 - 0, 15 - 8, 23 - 15 and return them.
# Complexity
# Time complexity is O(n), we traverse our string twice: one time when we evaluate
# ends and second time when we do partitions. Space complexity is O(26): to keep
# our ends (also we have answer, but it can not be greater than 26 as well).

# Code


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ends = {c: i for i, c in enumerate(s)}
        curr = 0
        ans = [0]
        while curr < len(s):
            end = ends[s[curr]]
            while curr <= end:
                end = max(end, ends[s[curr]])
                curr += 1
            ans.append(curr)
        return [ans[i] - ans[i-1] for i in range(1, len(ans))]
# Remark
# Note, that what we actually doing here is merging intervals, which is very
# similar to problem 0056 Merge Intervals, but here [1, 4] and [4, 5] is not
# overlapping. So, instead of [0, 2), [2, 4), we can use [0, 1.5], [2, 3.5] intervals
# and then just apply problem 0056 directly.
