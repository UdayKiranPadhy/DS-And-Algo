# Middle Element In 2-D Array

"""
Write a program that takes as input  2D Integer array and prints out the middle element in that 2d Array.

Input Format:

The first line take Integer inputs of row and colomn from stdin.
In Second line take the values of 2d array according to its row and colomn value.
Output Format:

Print the Integer which is middle element  in a 2d array .

Note: The Rows and Colomns length is odd always.

Example Input:

3 3
1 2 3
4 5 6
7 8 9

Output:
5

Example Input:

5 5
1 2 3 4 5
6 7 8 9 10
1 2 3 4 5
6 7 8 9 10
1 1 1 1 1

Output:
3


"""

# m, n = input().split(" ")
# m = int(m)
# n = int(n)
# list2 = []
# for i in range(m):
#     list2.append(input().split(" "))
# print(list2[int(m / 2)][int(n / 2)])

"""
3 3
1 2 3
1 2 3
1 2 3
[['1', '2', '3'], ['1', '2', '3'], ['1', '2', '3']]
2
"""

m = int(input())
n = int(input())
s = input().split(" ")
list2 = []
start = 0
for i in range(m):
    end = start + m
    list2.append(s[start:end])
    start = end
print(list2[int(m / 2)][int(n / 2)])
