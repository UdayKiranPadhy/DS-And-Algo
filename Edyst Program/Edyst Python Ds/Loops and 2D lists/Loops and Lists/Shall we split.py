"""
Estimated End Date: 18/02/21
Shall we split?
Complete the given method solve which takes as parameter a list A. We want to know whether the list can be split into 2 parts such that the sum of 1 side is equal to the sum of the other side.

If it's possible, print True. Otherwise, print False.

Example Input:
10 5 3 1 1 1 1 1 1 12

Output:
True

Explanation: The list can be split into [10,5,3] and [1,1,1,1,1,1,12] since both of their sums are equal

Example Input:
10 5 3 6

Output:
False

Explanation: The list cannot be split up into equal sums

Your Answer
"""
def solve(A):
    for i in range(1,len(A)):
        if sum(A[:i])==sum(A[i:]):
            print("True")
            break
    else:
        print("False")