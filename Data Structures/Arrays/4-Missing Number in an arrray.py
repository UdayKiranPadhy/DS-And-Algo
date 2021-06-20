"""
Missing number in array 
Easy
Given an array of size N-1 such that it can only contain distinct integers 
in the range of 1 to N. Find the missing element.

Example 1:

Input:
N = 5
A[] = {1,2,3,5}

Output: 4

Example 2:

Input:
N = 10
A[] = {1,2,3,4,5,6,7,8,10}

Output: 9

Your Task :
Complete the function MissingNumber() that takes array and N as input and returns the value of the missing number.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ N ≤ 106
1 ≤ A[i] ≤ 106

Company Tags
 Accolite Adobe Amazon Cisco D-E-Shaw Intuit Microsoft Morgan Stanley Ola Cabs Payu Qualcomm Visa
Topic Tags
 Arrays Bit Magic Searching

"""

# Hint1
"""
1. Return Difference of Summation of first N natural numbers 
and Summation of array elements
"""

# Solutuion
"""
Python
def MissingNumber(array,n):
    total = (n + 1)*(n)//2
    sum_of_A = sum(array)
    return total - sum_of_A


Java
// Back-end complete function Template for Java

class Solution {
    int MissingNumber(int array[], int n) {
        int i, total;
        total = (n + 1) * (n) / 2;
        for (i = 0; i < n-1; i++)
            total -= array[i];
        return total;
    }
}


// Back-end complete function template for C++

int MissingNumber(vector<int>& array, int n) {
    int total = (n + 1) * (n) / 2;
    for (int i = 0; i < n-1; i++)
        total -= array[i];
    return total;
}

"""


def MissingNumber(array, n):
    # code here
    return int(n * (n + 1) / 2 - sum(array))
