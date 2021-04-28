"""
Write a program that prints a simple chessboard. You have to read the the size of the chessboard from stdin. Print W for white spaces and B for black spaces.

Input format: size of the chessboard is given

Example Input:
3

Output:
WBW
BWB
WBW


Input:
5

Output:
WBWBW
BWBWB
WBWBW
BWBWB
WBWBW
"""

color = True
n = int(input())
if n % 2 == 0:
    for i in range(n):
        for j in range(n):
            if color:
                print("W", end="")
            else:
                print("B", end="")
            color = not color
        print()
        color = not color
else:
    for i in range(n):
        for j in range(n):
            if color:
                print("W", end="")
            else:
                print("B", end="")
            color = not color
        print()