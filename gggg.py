# Top to bottom


[[17, 14, 7, 0],
 [17, 14, 7, 0],
 [7, 7, 0, -1], 
 [0, 0, -1, 0]]

def Bombs(matrix,costA, costB):
    dp = [[-1 for _ in range(len(matrix[0]) + 1)]for __ in range(len(matrix) + 1)]
    print(dp)
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix[0])-1,-1):
            if i == len(matrix)-1 :
                return 0
            elif j == len(matrix[0]):
                return 0
            if ispresentHV(i,j):
                



print(Bombs([[0,0,0],[1,1,1],[0,1,0]],10,7))