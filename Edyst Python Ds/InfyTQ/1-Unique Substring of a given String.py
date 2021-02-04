"""
Given a string, we have to find the longest substring which is unique (that has no repetition) and whose 
size is at least 3.

If more than one substring is found with max length then we have to print the one which appeared first in 
the string

If no substring is present that matches the condition then we have to print -1

Example input: A@bcd1abx

Output: A@bcd1a
"""

str1=input()
str_temp=""
l=[]
i=0
while i < len(str1):
    if str1[i] in str_temp:
        l.append(str_temp)
        char = str1[i]
        str_temp=""
        i-=1
        while(char!=str1[i]):
            i-=1
    else:
        str_temp=str_temp+str1[i]
    i+=1
max_len=-1
for i in l:
    if len(i)>max_len:
        max_str=i
        max_len=len(i)
print(max_str)