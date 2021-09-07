from functools import lru_cache


def CollectMoney(input1,input2):

    # Code By akash
    @lru_cache(None)
    def move(i,j):
        if i<0 or i>= input1 or j <0 or j>= input1:
            return -99999999
        if i==input1-1 and j==input1-1:
            return input2[i][j]
        return input2[i][j] + max(move(i+1,j),move(i,j+1))
    
    return move(0,0)

input1 = 4
input2 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
print(CollectMoney(input1,input2))