"""
Let’s write the factorial of a number in a recursive manner.

Write a method Fac that takes as parameter an integer (n) and returns the Factorial of n. The Fac method has to be in a Solution class. Check the code editor for ideal method definition.

Note: n >= 0
Don’t write the Class and main method - assume they are already there.

Example
Input:
0
1
5
Output:
1
1
120
"""
class Solution:
    def Fac(self, n):
        if n<=1:
            return 1
        else:
            return n*Solution.Fac(self,n-1)