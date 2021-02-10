"""
Pronic Number
Pronic number is a number which is the product of two consecutive integers, that is, a number n is a product of x and (x+1).

Take a string in which random numbers are present and we have to find the product and the numbers(one is lesser and one is greater) which are already present in the string.also the numbers x and x+1 are single digit numbers. Let’s see the example:

E.g. Given a string contains 1203456. The multiplication of 3 and 4(one is lesser and one is greater) product become 12 and it’s present in the string. Like 4 and 5 (one is lesser and one is greater) the product is 20 and it’s present in the string and so on.

In such a way, We have to find all the numbers and in the output, we have to display the pronic numbers on a single line. Display only distinct numbers and make sure they are in sorted order.

If we haven’t found any product then print -1.
"""
n=input()
l=list(n)
f=[]
for i in range(len(n)):
    l[i]=int(l[i])

for i in range(len(l)):
    if l[i]+1 in l:
        if str(l[i]*(l[i]+1)) in n:
            f.append(l[i]*(l[i]+1))
f=list(set(f))
f.sort()
for i in range(len(f)):
    print(f[i],end=" ")
if len(f)==0:
    print(-1)