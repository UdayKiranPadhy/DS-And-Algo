"""
Equilibrium Point 
Easy 
Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
Equilibrium Point in an array is a position such that the sum of elements before it is equal to the 
sum of elements after it.

Example 1:
Input:
n = 1
A[] = {1}
Output: 1
Explanation: Since its the only 
element hence its the only equilibrium 
point. 

Example 2:
Input:
n = 5
A[] = {1,3,5,2,2}
Output: 3
Explanation: For second test case 
equilibrium point is at position 3 
as elements before it (1+3) = 
elements after it (2+2).
 

Your Task:
The task is to complete the function equilibriumPoint() which takes the array and n as input parameters 
and returns the point of equilibrium. Return -1 if no such point exists.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 106
1 <= A[i] <= 108

Company Tags
 Adobe Amazon
Topic Tags
 Arrays Prefix-sum
"""
# My Trail
def equilibriumPoint(A, N):
    if len(A)==1:
        return 1
    for i in range(len(A)-1):
        if sum(A[:i])==sum(A[i+1:]):
            return i+1
    return -1

# print(equilibriumPoint([1,3,5,2,2],5))

# Time limit exceeded .Need to go for prefix-sum algo to solve it
def equilibriumPoint2(A,n):
    