"""

problem Statement : https://codeforces.com/contest/1520/problem/E

E. Arranging The Sheep
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output

You are playing the game "Arranging The Sheep". The goal of this game is to 
make the sheep line up. The level in the game is described by a string of 
length n, consisting of the characters '.' (empty space) and '*' (sheep). 
In one move, you can move any sheep one square to the left or one square 
to the right, if the corresponding square exists and is empty. The game 
ends as soon as the sheep are lined up, that is, there should be no empty cells 
between any sheep.

For example, if n=6 and the level is described by the string "**.*..", then the 
following game scenario is possible:

the sheep at the 4 position moves to the right, the state of the level: "**..*.";
the sheep at the 2 position moves to the right, the state of the level: "*.*.*.";
the sheep at the 1 position moves to the right, the state of the level: ".**.*.";
the sheep at the 3 position moves to the right, the state of the level: ".*.**.";
the sheep at the 2 position moves to the right, the state of the level: "..***.";
the sheep are lined up and the game ends.
For a given level, determine the minimum number of moves you need to make to complete the level.

Input
The first line contains one integer t (1≤t≤10^4). Then t test cases follow.

The first line of each test case contains one integer n (1≤n≤10^6).

The second line of each test case contains a string of length n, consisting of the 
characters '.' (empty space) and '*' (sheep) — the description of the level.

It is guaranteed that the sum of n over all test cases does not exceed 106.

Output
For each test case output the minimum number of moves you need to make to complete the level.

Example
inputCopy
5
6
**.*..
5
*****
3
.*.
3
...
10
*.*...*.**
outputCopy
1
0
0
0
9

"""


def solve():
    n = input()
    string = input()
    left = 0
    right = len(string)-1
    dots = string.count(".")
    count = 0
    while left < right:
        if string[left] == "*" and string[right] == "*":
            count += dots
            left += 1
            right -= 1
        if string[left] == ".":
            left += 1
            dots -= 1
        if string[right] == ".":
            right -= 1
            dots -= 1
    print(count)


if __name__ == "__main__":
    from sys import *
    I = int
    R = range
    mod = 10000007
    # input = stdin.readline
    # print = stdout.writelines
    # listInput = [I(x) for x in input().strip().split()]
    # lineInput = (I(x) for x in input().strip().split())
    max_limit = float("inf")
    for i in R(I(input())):
        solve()
