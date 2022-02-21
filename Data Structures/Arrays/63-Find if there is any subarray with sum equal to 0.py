"""

Subarray with 0 sum 
Easy 
Given an array of positive and negative numbers. 
Find if there is a subarray (of size at-least one) with 0 sum.

Example 1:

Input:
5
4 2 -3 1 6

Output: 
Yes

Explanation: 
2, -3, 1 is the subarray 
with sum 0.
Example 2:

Input:
5
4 2 0 1 6

Output: 
Yes

Explanation: 
0 is one of the element 
in the array so there exist a 
subarray with sum 0.
Your Task:
You only need to complete the function subArrayExists() that takes array and n as parameters and returns true or false depending upon whether there is a subarray present with 0-sum or not. Printing will be taken care by the drivers code.

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).

https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1#

"""


class Solution:

    # Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self, arr, n):
        gg = {}
        s = 0
        for i in range(n):
            s = s + arr[i]
            if arr[i] == 0 or s in gg or s == 0:
                return "Yes"
            else:
                gg[s] = 1

# https://www.youtube.com/watch?v=xmguZ6GbatA&ab_channel=takeUforward
