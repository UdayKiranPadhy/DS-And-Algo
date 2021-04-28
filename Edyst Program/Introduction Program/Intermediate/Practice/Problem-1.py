# Consecutive Prime Sum

"""
Some prime numbers can be expressed as Sum of other consecutive prime numbers.
For example

5 = 2 + 3
17 = 2 + 3 + 5 + 7
41 = 2 + 3 + 5 + 7 + 11 + 13
Your task is to find out how many prime numbers which satisfy this property are present in 
the range 3 to N subject to a constraint that summation should always start with number 2.

Write code to find out number of prime numbers that satisfy the above mentioned property in a given range.

Input Format:
First line of input contains k - the number of inputs
The next k lines contains a number N.

Output Format:
Print the total number of all such prime numbers which are less than or equal to N.

Example:
Input:
k = 2
 
N = 20
 
N = 15
Output:
2 (there are 2 such numbers: 5 and 17)
1
"""
"""

def isPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def isCon(n):
    sum = 0
    for i in range(2, n):
        if isPrime2(i):
            sum += i
        if n == sum:
            return True
    return False


def isPrime2(n):
    if (n % 2 != 0) and (n % 3 != 0):
        return True
    return False

l = []
for i in range(int(input())):
    l.append(int(input()))
for i in l:
    count = 0
    if i < 5:
        print(0)
        continue
    else:
        for k in range(3, i):
            if isPrime2(k):
                if isCon(k):
                    count += 1
        print(count)
"""

# This Question was asked in TCS CodeVita 2016

# #include<iostream>
# using namespace std;
# int main(){
#         long long int num=0;
#         cout<<"Enter the Size to count Prime number till NUM : ";
#         cin>>num;
#         long long int ary[num],j=2;
#         ary[0] =2,ary[1]=3;
#         for(int i=2;i<=num;i++){      // loop will add the prime number till num
#                 if(i%2 != 0 && i%3 != 0){
#                     ary[j] = i;
#                         j++;
#                 }
#         }
#         long long int k,sum=0,count=0;
#         cout<<"Sum of Consecutive Prime numbers from "<<2<<" to "<<num<<endl;
#         for(int i=0;i<=j;i++){
#                 for(k=0;k<j;k++){
#                         sum+= ary[k];
#                         if(sum %2 !=0 && sum%3!=0 && sum<=num){
#                                 count++;
#                             cout<<sum<<endl;
#                         }
#                 }
#         }
#         cout<<"Total Consecutive Count : "<<count<<endl;
# }


# def isCon(n):
#     sum = 0
#     for i in range(2, n):
#         if isPrime(i):
#             sum += i
#         if n == sum:
#             return True
#     return False
"""
l = []
for i in range(int(input())):
    l.append(int(input()))
maxi = max(l)
sieve = [1] * (maxi + 1)
sieve[0] = sieve[1] = 0
prime = []
for i in range(2, maxi // 2):
    if sieve[i] == 1:
        prime.append(i)
    kn = i * i
    while kn < maxi:
        sieve[kn] = 0
        kn += i
con = []
sumi = 0
for i in prime:
    sumi += i
    if sumi > maxi:
        break
    if isPrime(sumi):
        con.append(sumi)
for i in l:
    count = 0
    for j in con:
        if j < i:
            count += 1
            # print(j)
        else:
            print(count)
            break
print(con)
print(prime)
"""

from math import sqrt


def isPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


# Function to return all prime numbers
def SieveOfEratosthenes(N):
    isprime = [True] * N
    isprime[0] = isprime[1] = False
    for p in range(2, int(sqrt(N)) + 1):

        # If prime[p] is not changed,
        # then it is a prime
        if isprime[p] == True:

            # Update all multiples of p greater
            # than or equal to the square of it
            # numbers which are multiple of p and are
            # less than p^2 are already been marked.
            for i in range(p * p, N, p):
                isprime[i] = False
    primes = []
    for i in range(2, N):
        if isprime[i]:
            primes.append(i)
    return primes


l = []
for _ in range(int(input())):
    l.append(int(input()))
for i in l:
    if i < 5:
        print("0")
        continue
    sum = 0
    con = []
    primes = SieveOfEratosthenes(i)
    for j in primes:
        sum += j
        if sum > i:
            break
        if isPrime(sum):
            con.append(sum)
    print(len(con))

"""
import math

def prime(s):
    if s==2 or s==3 or s==7 or s==11 or s==5:
        return True
    if s%2==0 or s%3==0 or s%7==0 or s%5==0 or s%11==0:
        return False
    d=math.floor(math.sqrt(s))
    if d>11:
        for i in range(11,d+1):
            if s%i==0:
                return False
    return True

def sumprime(a):
    d=[]
    c=0
    p=[2, 3]
    m=[5, 17, 41, 197, 281, 7699, 8893, 22039, 24133, 25237, 28697, 32353, 37561, 38921, 43201, 44683, 55837, 61027, 66463, 70241, 86453]
    if a<=99999:
        j=0
        while j<21:
            if m[j]<=a:
                c=c+1
            j=j+1
    else:
        c=c+21
        for i in range(99999,a):
            if prime(i):
                d.append(i)
                p.append(i) 
        for i in range(0,len(d)-1):
            j=0
            while(d[i] and j<len(d)):
                d[i]=d[i]-p[j]
                j=j+1
                if d[i]==0:
                    c=c+1
                    break
    return c
    
               
    
d=int(input())
g=[]
for i in range(0,d):
    g.append(int(input()))


for i in range(0,d):
    if g[i]<5:
        g[i]=0
    else:
        g[i]=sumprime(g[i])
        

for i in range(0,d):
    print(g[i])

"""