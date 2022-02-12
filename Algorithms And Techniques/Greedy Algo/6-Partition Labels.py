"""

763. Partition Labels
Medium


You are given a string s. We want to partition the string into as many parts as possible so 
that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the 
resultant string should be s.

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

"""


# https://leetcode.com/problems/partition-labels

# Solution
# The idea of this solution is greedily construct our partition, let us consider the
# example S = ababcbacde fegdehijhklij. We need to start with letter a and we can not
# stop, until we reach the last occurrence of a: so, we need to take ababcba part at
# least. But if we take this part, we need to consider letters b and c as well and
# also traverse our string until we meet the last occurrence of these letters, so
# we need to take ababcbac. Here we can stop, because we already take into account
# all symbols inside this string. So, we go to the next symbol and repeat our
# partition. So, what we have in my code:

# First, we need to know all ends for each letter in advance, I call it ends.
# Also, curr is current index and last is index we need to traverse until. For each
# group of symbols we need to do: last = ends[S[curr]]: we find the place we need to
# traverse; while we do no reach this place, we look at the next symbol and update
# our last. So, we stop, when curr become greater than last.
# We add curr to our out result.
# Note, that we need to have [8, 7, 8] for our example, but we get [8, 15, 23],
# places where our partitions are. So, we evaluate differences 8 - 0, 15 - 8, 23 - 15 and return them.

# Complexity
# Time complexity is O(n), we traverse our string twice: one time when we
# evaluate ends and second time when we do partitions.
# Space complexity is O(26): to keep our ends (also we have answer, but it can
# not be greater than 26 as well).

class Solution:
    def partitionLabels(self, S):
        ends = {c: i for i, c in enumerate(S)}
        curr, out = 0, [0]

        while curr < len(S):
            last = ends[S[curr]]
            while curr <= last:
                symb = S[curr]
                last = max(last, ends[symb])
                curr += 1
            out.append(curr)

        return [out[i]-out[i-1] for i in range(1, len(out))]


# How about an approach using intervals. Compute interval (start, end)
# for each letter [a-z] , where start is first occurrence of letter, and end is last
# occurrence of letter. Then we merge any overlapping intervals, and the resulting
# intervals can form the answer.
