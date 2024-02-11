"""

https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1

Row with max 1s
MediumAccuracy: 33.09%Submissions: 233K+Points: 4
Internship Alert!
Become an SDE Intern by topping this monthly leaderboard!

banner
Given a boolean 2D array of n x m dimensions, consisting of only 1's and 0's, where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

Example 1:

Input:
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).

Example 2:

Input:
N = 2, M = 2
Arr[][] = {{0, 0}, {1, 1}}
Output: 1
Explanation: Row 1 contains 2 1's (0-based
indexing).

Your Task:
You don't need to read input or print anything. Your task is to complete the function rowWithMax1s() which takes the array of booleans arr[][], n and m as input parameters and returns the 0-based index of the first row that has the most number of 1s. If no such row exists, return -1.


Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N, M ≤ 103
0 ≤ Arr[i][j] ≤ 1

"""


class Solution:
    def rowWithMax1s(self,arr, R, C):
        max_row = -1
        index = C-1
        for i in range(R):
            prev_index = index
            if arr[i][index] == 1:
                while index >= 0 and arr[i][index] == 1:
                    index -=1
                if index<0:
                    return i
                if prev_index != index:
                    max_row = i
        return max_row
