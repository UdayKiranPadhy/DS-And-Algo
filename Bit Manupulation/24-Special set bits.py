"""

Special Set bits
You are given a set of numbers. Using the binary representation of all the numbers from L to R and have to count the special ones on the list.

Important notes:

A bit is called to be set if it has value 1
The special one is a set bit in the binary representation of any number X where L<=X < =R 
and this bit is at prime index in the binary representation of X.
The positioning of the bits is done from right to left and starts from 1.
For example, the binary representation of 4 is 100. In this, 1st and 2nd bits are not set 
while 3rd bit is set. Also, this 3rd bit is a special one because 3 is a prime number.

Input format:

First line of input contains a single integer T denoting the number of test cases
T lines follow each containing two space-separated integer L and R
Output format:

For each test case, print a single integer denoting the number of special 1's on the list.

Constraints:

1 <= L <= R <= 106
1 < T < 103

"""

# My trail 

# for _ in range(int(input())):
#     l = list(map(int, input().split(" ")))
#     count = 0
#     for i in range(l[0], l[1] + 1):
#         gg = i & 332886
#         count += bin(gg).count("1")
#     print(count)




# Solution which is accepted
def isPrime(n):
    if(n<=1):
        return False
    if(n<=3):
        return True
    if(n%2==0 or n%3==0):
        return False
    i=5
    while(i*i<=n):
        if(n%i==0 or n%(i+2)==0):
            return False
        i+=6
    return True
  
def countSpecial(n):
    i=1
    c=1
    counter=0
    while(i<=n):
        if(isPrime(c) and (n&i)!=0):
            counter+=1
        c+=1
        i*=2
    return counter
def setCount(mx):
    li=[0]*(mx+1)
    for i in range(mx+1):
        li[i]=countSpecial(i)
    return li
    
if __name__=='__main__':
    t=int(input())
    L=[]
    R=[]
    mx=0
    for kk in range(t):
        a,b=map(int,input().split())
        if(mx<b):
            mx=b
        L.append(a)
        R.append(b)
    res=setCount(mx)
    for i in range(len(L)):
        print(sum(res[L[i]:R[i]+1]))