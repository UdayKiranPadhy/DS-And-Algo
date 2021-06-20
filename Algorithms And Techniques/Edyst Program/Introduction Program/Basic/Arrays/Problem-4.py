# Largest Palindrome in the Array

"""

Write a program to find the largest palindrome in the String Array

Input Format:

In First line take an Integer which is size of the array
In Second line take a list of Strings
Output Format:

print the Largest palindrome String

Example Input:
4
aba abab abaab abaaba

Output:
abaaba

Note:

If there are multiple largest palindromic strings with same length, print the lexicpraphically smallest one.

"""


def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


n = int(input())
s = input().split(" ")
max = 0
o = ""
for i in s:
    if palindrome(i):
        if len(i) > max:
            max = len(i)
            o = i
if max == 0:
    print("-1")
else:
    print(o)


# Transpose of matrix
# #include<iostream>
# #include<bits/stdc++.h>

# using namespace std;

# int main()
# {
#     int r,c;
#     cin>>r>>c;
#     int a[r][c],b[r][c];
#     for(int i=0;i<r;i++)
#     {
#         for(int j=0;j<c;j++)
#         {
#             cin>>a[i][j];
#         }
#     }
#  	   for(int i=0;i<r;i++)
#     {
#         for(int j=0;j<c;j++)
#         {
#             b[j][i]=a[i][j];
#         }
#     }
#      for(int i=0;i<r;i++)
#     {
#         for(int j=0;j<c;j++)
#         {
#             cout<<b[i][j]<<" ";
#         }
#          cout<<endl;
#     }
# }

# Sum of elements
# n = int(input())
# l = input().split(" ")
# sum=0
# for i in l:
#     sum += int(i)
# print(sum)


# n = int(input())
# s = input()
# n= int(input())
# s += " "
# s += input()
# l=s.split(" ")
# l2 = []
# for i in l:
#     l2.append(int(i))
# l2.sort()
# for i in l2:
#     print(i, end=" ")


# def reverseWord(Str):
#     i = 1
#     j = len(Str) - 2
#     while (i < j):
#         Str[i],Str[j]=Str[j],Str[i]
#         i += 1
#         j -= 1

#     return "".join(Str)
# def reverseWords(Str):
#     Str = Str.split()
#     for i in Str:
#         j = [h for h in i]
#         print(reverseWord(j), end = " ")
# t=int(input())
# for i in range(t):
#     s=input()
#     reverseWords(s)
#     print()