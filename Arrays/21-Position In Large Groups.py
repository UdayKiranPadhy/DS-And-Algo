"""

830. Positions of Large Groups
Easy
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start 
and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.

 

Example 1:

Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.
Example 2:

Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.
Example 3:

Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".
Example 4:

Input: s = "aba"
Output: []
 

Constraints:

1 <= s.length <= 1000
s contains lower-case English letters only.

"""


def largeGroupPositions(self, S):
    i, j, N = 0, 0, len(S)
    res = []
    while i < N:
        while j < N and S[j] == S[i]:
            j += 1
        if j - i >= 3:
            res.append([i, j - 1])
        i = j
    return res

# My Trails Unsuccesful


class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        left = 0
        right = 0
        start = 0
        end = 0
        count = 0
        end += 1
        ans = []
        while end < len(s):
            if s[start] == s[end]:
                end += 1
                count += 1
                if count > 2:
                    left = start
                    right = end-1
                    ans.append([left, right])
            else:
                start = end
                end += 1
                count = 0
        return ans


model = Solution()
print(model.largeGroupPositions("abbxxxxzzy"))


"""
Solution
Approach #1: Two Pointer [Accepted]
Intuition

We scan through the string to identify the start and end of each group. 
If the size of the group is at least 3, we add it to the answer.

Algorithm

Maintain pointers i, j with i <= j. The i pointer will represent the 
start of the current group, and we will increment j forward until it 
reaches the end of the group.

We know that we have reached the end of the group when j is at the 
end of the string, or S[j] != S[j+1]. At this point, we have some 
group [i, j]; and after, we will update i = j+1, the start of the next group.


class Solution(object):
    def largeGroupPositions(self, S):
        ans = []
        i = 0 # The start of each group
        for j in xrange(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans


Complexity Analysis

Time Complexity: O(N), where N is the length of S.

Space Complexity: O(N), the space used by the answer.


"""
