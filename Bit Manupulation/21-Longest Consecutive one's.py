"""
Longest Consecutive 1's 
Given a number N. Find the length of the longest consecutive 1s in its 
binary representation.

Example 1:
Input: N = 14
Output: 3
Explanation: 
Binary representation of 14 is 
1110, in which 111 is the longest 
consecutive set bits of length is 3.

Example 2:
Input: N = 222
Output: 4
Explanation: 
Binary representation of 222 is 
11011110, in which 1111 is the 
longest consecutive set bits of length 4. 

Your Task: 
You don't need to read input or print anything. Your task is to complete 
the function maxConsecutiveOnes() which returns the length of the 
longest consecutive 1s in the binary representation of given N.

Expected Time Complexity: O(log N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 106
"""

# Keep assigning the value of N&(N<<1) to N untill N becomes 0.

#  The idea is based on the concept that if we AND a bit sequence with a
# left shifted version of itself, we’re effectively removing the trailing
# 1 from every sequence of consecutive 1s.
#   11101111   (N)
# & 11011110   (N << 1)
# ----------
#   11001110   (N & (N << 1))
# ^    ^
# |    |
#    trailing 1 removed
# So the operation N = (N & (N << 1)) reduces length of every sequence
# of 1s by one in binary representation of N. If we keep doing this
# operation in a loop, we end up with N = 0. The number of iterations
# required to reach 0 is actually length of the longest consecutive
# sequence of 1s.


class Solution:
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, N):
        count = 0
        # We use a loop to perform AND operation on N and N<<1 and everytime
        # the trailing 1 from every sequence of consecutive 1s is removed.
        # Loop continues till N is reduced to 0.
        while N != 0:
            # Assigning result of AND operation to N
            N = N & (N << 1)
            # increment of counter variable.
            count += 1

        # returning the answer.
        return count


# https://practice.geeksforgeeks.org/problems/longest-consecutive-1s-1587115620/1