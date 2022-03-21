"""
Problem Statement : https://practice.geeksforgeeks.org/problems/find-first-set-bit-1587115620/1#

Find first set bit 

Given an integer an N. The task is to return the position of first set bit found from the right side in the binary representation of the number.
Note: If there is no set bit in the integer N, then return 0 from the function.  

Example 1:

Input: N = 18
Output: 2
Explanation: Binary representation of 
18 is 010010,the first set bit from the 
right side is at position 2.
Example 2:

Input: N = 12 
Output: 3 
Explanation: Binary representation 
of  12 is 1100, the first set bit 
from the right side is at position 3.
Your Task:
The task is to complete the function getFirstSetBit() that takes an integer n as a parameter and returns the position of first set bit.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
0 <= N <= 10^8

"""

# My Trails Success
import math


class Solution:

    # Function to find position of first set bit in the given number.
    def getFirstSetBit(self, n):
        if n == 0:
            return 0
        binary = bin(n)[2:]
        index = 1
        for i in range(len(binary)-1, -1, -1):
            if binary[i] == '1':
                index = i
                break
        return len(binary) - index


# Actual Procedure
"""
Hint 1
Take two's complement of the given no as all bits are reverted
except the first '1' from right to left

Hint2
AND operation of n and -n gives 1 only at the position of first
set bit and rest bits becomes zero.

Then find log2 of the result and add 1 to get the answer.
"""


class Solution:

    # Function to find position of first set bit in the given number.
    def getFirstSetBit(self, n):
        if(n == 0):
            return 0

        # doing AND operation of n and -n. n and -n will have similar
        # bits only till the first set bit starting from the right
        # and differnt bits after the first set bit.Then we take
        # log2 of the result to find the position.

        # we add 1 to obtained value so that count starts from 1 instead of 0.
        return math.ceil(math.log2(n & -n)+1)


""" C++

class Solution
{
    public:
    //Function to find position of first set bit in the given number.
    unsigned int getFirstSetBit(int n)
    {
        //doing AND operation of n and -n. n and -n will have similar
        //bits only till the first set bit starting from the right  
        //and differnt bits after the first set bit.Then we take 
        //log2 of the result to find the position.
        
        //we add 1 to obtained value so that count starts from 1 instead of 0.
        return log2(n&-n)+1; 
              
    }
};



"""
