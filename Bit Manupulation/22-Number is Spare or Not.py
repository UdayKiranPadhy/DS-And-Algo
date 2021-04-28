"""
Number is sparse or not 

Given a number N. The task is to check whether it is sparse or not. 
A number is said to be a sparse number if no two or more consecutive 
bits are set in the binary representation.

Example 1:
Input: N = 2
Output: true
Explanation: Binary Representation of 2 is 10, 
which is not having consecutive set bits. 
So, it is sparse number.

Example 2:
Input: N = 3
Output: false
Explanation: Binary Representation of 3 is 11, 
which is having consecutive set bits in it. 
So, it is not a sparse number.

Your Task: The task is to complete the function checkSparse() that 
takes n as a parameter and returns true if the number is sparse 
else returns false.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 10^6
"""

# Just see if two or more consecutive bits are set or not using n&(n>>1)


def spare(n: int) -> int:
    return not n & (n >> 1)


print(spare(2))