"""
Kadane's Algorithm 
Medium 
Given an array arr of N integers. 
Find the contiguous sub-array with maximum sum.
 

Example 1:

Input:
N = 5
arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
Example 2:

Input:
N = 4
arr[] = {-1,-2,-3,-4}
Output:
-1
Explanation:
Max subarray sum is -1 
of element (-1)
 

Your Task:
You don't need to read input or print anything. The task is to complete the function maxSubarraySum() which takes arr and N as input parameters and returns the sum of subarray with maximum sum.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

 

Constraints:
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Company Tags
 24*7 Innovation Labs Accolite Amazon Citrix D-E-Shaw FactSet Flipkart Hike Housing.com MetLife Microsoft Morgan Stanley Ola Cabs Oracle Payu Samsung Snapdeal Teradata Visa Walmart Zoho
Topic Tags
 Arrays Dynamic Programming Algorithms

https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
"""
# Maximum ending here
# Maximum So Far
def maxSubArraySum(a,size):
    ##Your code here
    msf=0
    meh=0
    for i in a:
        meh=meh + i
        if meh <i:
            meh = i
        if msf < meh:
            msf = meh
    return msf
