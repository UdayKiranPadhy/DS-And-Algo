# [Google] Add One To Number

"""
You are given a non-negative number represented as an array of digits.
Example: 123 is represented as [1,2,3]

You must add 1 to the number ( increment the number represented by the digits ) and return the 
required array or list.

The digits are stored such that the most significant digit is at the head of the list.
Example:
If the vector has [1, 2, 3], the returned vector should be [1, 2, 4],
as 123 + 1 = 124.

Some notes:
Your returned array must not have any leading zeros. Example:
Input:
[0,0,2,1]
 
Ouput:
[2,2] // no leading zeros
Maximum size of the array is 300 so avoid converting it to a string or an integer. 
Instead, try to think of what happens when 1 is added to the number.
"""

# Approach
"""
To add 1 to a number x (say 0011000111), flip all the bits after the rightmost 0 bit (we get 0011000000). 
Finally, flip the rightmost 0 bit also (we get 0011001000) to get the answer.


Reverse the digits of the number to make your life easier.

Maintain a carry which is initialized to 1 ( Denoting that we need to add one to the number ).
Run a loop on the digit array ( which is now reversed ), and add carry to the current digit. If the digit D exceeds 10 on doing so, store the last digit in current position ( D % 10 ), and make carry = rest of the digits ( D / 10 ). Continue the process till you have covered all the digits.
Now if at the end, carry = 0, we are done, and we can return the array.

If not, we need to add one more digit, with carry in it.
"""


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        for i in range(len(A) - 1, -1, -1):
            if A[i] == 9:
                A[i] = 0
            else:
                A[i] += 1
                while True:
                    if A[0] == 0:
                        del A[0]
                    else:
                        return A
                return A

        A = [1] + A
        return A