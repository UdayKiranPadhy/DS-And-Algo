"""

Problem Statement :- https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1

Longest consecutive subsequence
MediumAccuracy: 33.0%Submissions: 278K+Points: 4
Internship Alert!
Become an SDE Intern by topping this monthly leaderboard!

banner
Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.


Example 1:

Input:
N = 7
a[] = {2,6,1,9,4,5,3}
Output:
6
Explanation:
The consecutive numbers here
are 1, 2, 3, 4, 5, 6. These 6
numbers form the longest consecutive
subsquence.
Example 2:

Input:
N = 7
a[] = {1,9,3,10,4,20,2}
Output:
4
Explanation:
1, 2, 3, 4 is the longest
consecutive subsequence.

Your Task:
You don't need to read input or print anything. Your task is to complete the function findLongestConseqSubseq() which takes the array arr[] and the size of the array as inputs and returns the length of the longest subsequence of consecutive integers.


Expected Time Complexity: O(R), where R is the maximum integer in the array.
Expected Auxiliary Space: O(N).


Constraints:
1 <= N <= 105
0 <= a[i] <= 105

"""


# Failed
class Solution:
    def findLongestConseqSubseq(self, arr, N):
        seen = {}
        for ind, val in enumerate(arr):
            seen[val] = 1
        cons = {}
        max_con = 0
        for i in arr:
            if i in seen:
                seen[i] = seen[i-1] + 1
                max_con = max(max_con,seen[i])
            else:
                seen[i]=1
        return max_con