"""
Min XOR Value
Given an array of N integers, find the pair of integers in the array 
which have minimum XOR value. Report the minimum XOR value.

Examples :
Input
0 4 3 9
Output
3 (0 XOR 3)

Input
0 8 7 10
Output
2 (8 XOR 10)

Constraints:
2 <= N <= 100 000
0 <= A[i] <= 1 000 000 000
"""




# Solution
"""
Exploring XOR
Let us say we are taking the XOR of 2 pairs
A^B, A^C

And it is given that, A > B > C.
Then, can we make any conclusions about A^B and A^C. 
is A^B > A^C? or is A^B < A^C?

Let’s look at the nature of XOR to understand that.
Let’s say we have
A = …00000XXXX
B = …00000XXXX
C = …00000XXXX

Since B is closer to A than C, we are going to have a bit set closer to 
the left of B, than in C.
That is, a more significant bit of B will be set as compared to C.
Let’s understand what that means, with an example:
A = 10111 (23)
B = 10001 (17)
C = 01001 (9)
Since the more significant bit of B is set as compared to C, 
the resultant XOR will be of a lesser value because the the XOR will 
unset that particular bit.

Thus, if we were to check the values of XOR for a particular number, 
we need NOT check all the XOR pairs.
Instead, we only need to check for the number closest to it.
How do we do that?
We can simply sort the array! The array sorting happens in O(nlogn) time. 
Then we only consider those pairs of numbers that are adjacent to each other.

Efficient Approach
The pseudo-code for the same is:

sort(A) //O(nlogn)
min = 0
    for i: 0 to N-1 // O(n)
        if (A[i] ^ A[i+1] < min)
            min  = A[i] ^ A[i+1]
return min
"""

class Solution:
    def findMinXor(self, A):
        A.sort()
        min=9999999
        for i in range(len(A)-1):
            if (A[i]^A[i+1]<min):
                min = A[i]^A[i+1]
                pos = i
        return min