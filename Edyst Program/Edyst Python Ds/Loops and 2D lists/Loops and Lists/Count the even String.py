"""
Count the even strings
Complete the given function solve, which takes a list A as parameter, you have to return the number of strings in that list that have even length

Example Input:
my code is beautiful and so is edyst

Output:
5
"""
def solve(A):
    count=0
    for i in A:
        if len(i)%2==0:
            count+=1
    return count