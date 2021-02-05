"""
Your task here is to take input a string and reverse it. 
However, you should reverse only the normal alphabets. 
The special characters should be in their original positions.

Example Input
sd&hg#j
 
Output
jg&hd#s
"""
k=input()
l=[]
for i in k:
    if i.isalpha():
        l.append(i)
l=l[::-1]
string="".join(l)
for i in range(len(k)):
    if k[i].isalpha():
        continue
    else:
        string=string[:i]+k[i]+string[i:]
print(string)
