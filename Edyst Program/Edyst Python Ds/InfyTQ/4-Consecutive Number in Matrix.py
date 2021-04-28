"""

You are given an m*n matrix such that n = m+1. In the given matrix, find if any number is consecutive for 3 times either in row, column, diagonals print the num.

If there are multiple such numbers then print minimum of those numbers.

Input format
First line contains m, the number of rows
Following m lines contain n numbers
Example Input

6
2 3 4 5 6 2 4
2 3 4 7 6 7 6
2 3 5 5 5 5 2
2 3 1 1 2 1 3
1 1 1 1 9 0 3
2 3 1 1 5 1 2
Output

1

"""
def checkbottom(matrix,i,j):
    if i+2>=len(matrix):
        return False
    if matrix[i][j]==matrix[i+1][j]==matrix[i+2][j]:
        return True
    return False

def checktop(matrix,i,j):
    if i-2<0:
        return False
    if matrix[i][j]==matrix[i-1][j]==matrix[i-2][j]:
        return True
    return False

def checkright(matrix,i,j):
    if j+2>=len(matrix[0]):
        return False
    if matrix[i][j]==matrix[i][j+1]==matrix[i][j+2]:
        return True
    return False

def checkleft(matrix,i,j):
    if j-2<0:
        return False
    if matrix[i][j]==matrix[i][j-1]==matrix[i][j-2]:
        return True
    return False

def checkdiagnal(matrix,i,j):
    if j-2>0 and i-2>0:
        if matrix[i][j]==matrix[i-1][j-1]==matrix[i-2][j-2]:
            return True
    if j+2<len(matrix[0]) and i+2<len(matrix):
        if matrix[i][j]==matrix[i+1][j+1]==matrix[i+2][j+2]:
            return True
    if i-2>0 and j+2<len(matrix[0]):
        if matrix[i][j]==matrix[i-1][j+1]==matrix[i-2][j+2]:
            return True
    if i+2<len(matrix) and j-2>0:
        if matrix[i][j]==matrix[i+1][j-1]==matrix[i+2][j-2]:
            return True
    return False
    
m=10
m=int(input())
n=m+1
numbers = []
matrix=[]
for i in range(m):
    list1=list(map(int,input().split(" ")))
    matrix.append(list1)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if checktop(matrix,i,j):
            numbers.append(matrix[i][j])
        if checkbottom(matrix,i,j):
            numbers.append(matrix[i][j])
        if checkright(matrix,i,j):
            numbers.append(matrix[i][j])
        if checkleft(matrix,i,j):
            numbers.append(matrix[i][j])        
        if checkdiagnal(matrix,i,j):
            numbers.append(matrix[i][j])
print(min(numbers))