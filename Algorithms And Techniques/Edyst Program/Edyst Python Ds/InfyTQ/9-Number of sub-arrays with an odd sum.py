"""
Given an array, find the number of sub-arrays whose sum is odd.

Input Format
First line contains the size of the array.
second line the list of elements, separated by space

Output Format:
print the number of sub arrays who sum is odd

Example Input
5 4 4 5 1 3

Output
12

Explanation
These are possible subarrays with odd sum:
5 Sum = 5 (At index 0)
5, 4  Sum = 9
5, 4, 4  Sum = 13
5, 4, 4, 5, 1 Sum = 19
4, 4, 5  Sum = 13
4, 4, 5, 1, 3  Sum = 17
4, 5  Sum = 9
4, 5, 1, 3 Sum = 13
5  Sum = 5 (At index 3)
5, 1, 3  Sum = 9
1 Sum = 1
3 Sum = 3

"""
_=input()
l=list(map(int,input().split(" ")))
count=0
for i in range(len(l)):
    for j in range(i,len(l)+1):
        if sum(l[i:j])%2!=0:
            count+=1
print(count)