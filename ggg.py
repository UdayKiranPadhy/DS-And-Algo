def ispresentHV(i, j):
    global matrix
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


def ispresentV(i, j):
    global matrix
    Vertical = False
    for gg in range(i, len(matrix)):
        if matrix[gg][j] == 1:
            Vertical = True
            break
    return Vertical


def ispresentH(i, j):
    global matrix
    Horizontal = False
    for gg in range(j, len(matrix[0])):
        if matrix[i][gg] == 1:
            Horizontal = True
            break
    return Horizontal


def Bombs(i, j):
    global matrix
    global costA
    global costB
    if dp[i,j] == -1:
        if i >= len(matrix) or j >= len(matrix[0]):
            dp[i][j] =0
            return dp[i][j]
        elif ispresentHV(i, j):
            return min(costA + Bombs(i + 1, j), costB + Bombs(i, j + 1))
        elif ispresentH(i, j):
            return min(costA + Bombs(i + 1, j), Bombs(i, j + 1))
        elif ispresentV(i, j):
            return min(costB + Bombs(i, j + 1), Bombs(i + 1, j))
        else:
            return Bombs(i + 1, j + 1)
    else:
        return dp[i][j]

costA = 10
costB = 7
matrix = [[0, 0, 0], [1, 1, 1], [0, 1, 0]]
dp = [[-1 for _ in range(len(matrix[0])+1)] for __ in range(len(matrix)+1)]
print(Bombs(0, 0))
