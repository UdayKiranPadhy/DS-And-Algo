"""

Given a N * M grid, some cells of the grid are empty while the others
contain enemy units. You must kill all the enemies using two kinds of
bombs:
1) First type kills all the enemy units in some row and costs A USD
2) Second type kills all the enemy units in some column and costs
B USD.

You have infinite number of bombs of each type and your task is to find
the minimum cost to kill all enemy units.

Input Format
The first line contains an integer, N, denoting the number of rows in Arr.
The next line contains an integer, M. denoting the number of columns
In Arr
The next line contains an integer A denoting the cost of first type
bomb
The next line contains an integer, B, denoting the cost of second type
bomb.
Each line i of the N subsequent lines (where 0 <= i < N) contains M
space separated integers each describing the row Arr[i].

Constraints
1 <=N <= 10
1 <= M <= 10^3
1 <= A <= 10^6
1 <= B <= 10^6
0 <= Arr[i][j] <= 1


Sample Input:
3
3
15
7
0 0 0
1 1 1
0 1 0

output : 21  
Explainataiom: Use three bombs of the second type with each column total 
cost = 7 * 3 = 21


3
3
10
13
0 0 0
1 1 1
0 1 0

output: 20

explanatation: 
Use two bombs of 1st type with the second and 3rd rows
total cost = 10*2 = 20


3
3
10
7
0 0 0
1 1 1
0 1 0

output: 17

Explanatation:
Use 1st type bomb with second row , and second type bomb
with the second column
total cost = 10 + 7
"""


def ispresentHV(matrix, i, j):
    Horizontal = False
    Vertical = False
    for gg in range(i, len(matrix)):
        if matrix[gg][j] == 1:
            Horizontal = True
            break
    for gg in range(j, len(matrix[0])):
        if matrix[i][gg] == 1:
            Vertical = True
            break
    if Vertical and Horizontal:
        return True
    else:
        return False


def ispresentV(matrix, i, j):
    Vertical = False
    for gg in range(i, len(matrix)):
        if matrix[gg][j] == 1:
            Vertical = True
            break
    return Vertical


def ispresentH(matrix, i, j):
    Horizontal = False
    for gg in range(j, len(matrix[0])):
        if matrix[i][gg] == 1:
            Horizontal = True
            break
    return Horizontal


def Bombs(matrix, i, j, costA, costB):
    global dp
    if dp[i][j] == -1:
        if i >= len(matrix) or j >= len(matrix[0]):
            dp[i][j] = 0
            return dp[i][j]
        elif ispresentHV(matrix, i, j):
            dp[i][j] = min(
                costA + Bombs(matrix, i + 1, j, costA, costB),
                costB + Bombs(matrix, i, j + 1, costA, costB),
            )
            return dp[i][j]
        elif ispresentV(matrix, i, j):
            dp[i][j] = min(
                costA + Bombs(matrix, i, j + 1, costA, costB),
                Bombs(matrix, i + 1, j, costA, costB),
            )
            return dp[i][j]
        elif ispresentH(matrix, i, j):
            dp[i][j] = min(
                costB + Bombs(matrix, i + 1, j, costA, costB),
                Bombs(matrix, i, j + 1, costA, costB),
            )
            return dp[i][j]
        else:
            dp[i][j] = Bombs(matrix, i + 1, j + 1, costA, costB)
            return dp[i][j]
    else:
        return dp[i][j]


N = int(input())
M = int(input())
costA = int(input())
costB = int(input())
matrix = []
for i in range(N):
    gg = input()
    matrix.append(list(map(int, gg.split(" "))))
dp = [[-1 for _ in range(len(matrix[0]) + 1)] for __ in range(len(matrix) + 1)]
print(Bombs(matrix, 0, 0, costA, costB))
