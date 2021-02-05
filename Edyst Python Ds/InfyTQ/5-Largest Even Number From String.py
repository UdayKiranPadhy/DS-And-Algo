"""
Take as input a string. This string is a mixture of letters, integers and special char. 
From this string, find the largest even number that can pe possibly formed after removing the duplicates.
If an even is not formed then return -1.

Example Input
infosys@337

Output
-1

Explanation

No even number can be formed

Example Input
Hello#81@21349

Output
984312

"""
k=input()
l=[]
for i in k:
    if i.isdigit():
        if int(i) not in l:
            l.append(int(i))
l.sort(reverse=True)
print(l)