"""
Triangle of Alphabets

Write a program that reads an input n from stdin. n tells us the number of rows to be printed. Print the pattern as per the given examples.

Input format: The first line contains the number of inputs. The lines after that contain a different values for n

Note: You have to write the entire program and not just the single function!

Example Input:
2
3
5

Output:
A
BB
CCC
A
BB
CCC
DDDD
EEEEE
"""
Alphabets = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
}
for i in range(int(input())):
    n = int(input())
    for i in range(1, n + 1):
        for j in range(i):
            print(Alphabets[i], end=" ")
        print()