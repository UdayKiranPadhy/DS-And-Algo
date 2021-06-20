"""
Check if list is in AP
Complete the given method solve. You are given a list of integers A. You have to check whether the list forms an AP (Arithmetic Progression or not). Print True if it does and Normal Series if it does not.

Example Input:
1 6 11 16 21

Output:
True

Example Input:
9 0 7 1 5

Output:
Normal Series
"""

def solve(A):
    cd=A[1]-A[0]
    for i in range(1,len(A)-1):
        if (A[i]+cd==A[i+1]):
            continue
        else:
            print("Normal Series")
            break
    else:
        print("True")