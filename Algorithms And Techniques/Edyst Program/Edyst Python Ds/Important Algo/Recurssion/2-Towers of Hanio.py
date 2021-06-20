"""
As per the constraints of the Towers of Hanoi, write a method Met that takes 4 parameters:

First, an integer with number of discs
Second, a String with name of starting pole
Third, a String with name of helper pole
Fourth, a String with name of destination pole
You have to print the steps to solve the problem.

The Met method has to be inside a Solution class. Please check the code editor for the ideal method definition.

Example Input:
3 A B C
Output:
A to C
A to B
C to B
A to C
B to A
B to C
A to C
"""


class Solution:
    def Met(self, discs, start, helper, destination):
        if discs == 1:
            print(start + " to " + destination)
        else:
            Solution.Met(self, discs - 1, start, destination, helper)
            print(start + " to " + destination)
            Solution.Met(self, discs - 1, helper, start, destination)
