"""
Maximum subset XOR 
Given an array arr[] of N positive integers. Find an integer denoting 
the maximum XOR subset value in the given array arr[].

Example 1:
Input : 
N = 3
arr[] = {2, 4, 5}
Output : 7
Explanation : 
The subset {2, 5} has maximum 
subset XOR value.

Example 2 :
Input : 
N= 3
arr[] = {9, 8, 5}
Output : 13
Explanation : 
The subset {8, 5} has maximum 
subset XOR value.
Your task :
You don't need to read input or print anything. Your task is to complete 
the function maxSubarrayXOR() which takes the array and an integer as 
input and returns the maximum subset XOR value.
 
Expected Time Complexity : O(N*Log(max(arr[i])))
Expected Auxiliary Space : O(1)
 
Contraints :
1 <= N <= 10^5
1 <= arr[i] <= 10^6
"""