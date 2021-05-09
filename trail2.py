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
print(dp)
