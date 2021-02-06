"""
You are given a list of tuples, called list1. Each tuple has 2 elements signifying the length and 
the breadth of a rectangle.
Some rectangles may be of same area, while other may result in a different area.
Your task is to list down all possible areas, and the frequency of each area. 
Print in ascending order of areas.

Example Input
[(1, 4), (2, 3), (2, 2), (10, 2), (4, 5)]

Output
4: 2
6: 1
20: 2

Complete the given method solve which takes as parameter a list called list. You don't have to take any input. Just print the output as per the given format.
"""
def solve(list1):
    d={}
    for i in list1:
        x,y=i
        if x*y in d:
            d[x*y]+=1
        else:
            d[x*y]=1
    for i in sorted(d):
        print(str(i)+": "+str(d[i]))