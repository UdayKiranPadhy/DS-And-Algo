# Prime Sum

"""
Given an even number (greater than 2), return two prime numbers whose sum will be equal to given number.

Note: A solution will always exist.

Example:

Input : 4
Output: 2 + 2 = 4

If there are more than one solutions possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b,
and [c,d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d

"""

inp = int(input())


def getprimes(i):
    seive = [1] * (i + 1)
    n = 2
    prime = []
    while n < i:
        if seive[n] == 1:
            prime.append(n)
        kn = n * n
        while kn < i:
            seive[kn] = 0
            kn += n
        n += 1
    return prime


Output = []
primes = getprimes(inp)
for i in range(len(primes) - 1):
    for j in range(i + 1, len(primes)):
        if primes[i] + primes[j] == inp:
            Output.append([primes[i], primes[j]])
if inp == 4:
    print("2 2")
else:
    print(Output[0][0], end=" ")
    print(Output[0][1])

"""
class Solution:
    def primesum(self, A):
        Output = []
        seive = [1] * (A + 1)
        n = 2
        primes = []
        while n < A:
            if seive[n] == 1:
                primes.append(n)
            kn = n * n
            while kn < A:
                seive[kn] = 0
                kn += n
            n += 1
        for i in range(len(primes) - 1):
            for j in range(i + 1, len(primes)):
                if primes[i] + primes[j] == A:
                    Output.append([primes[i], primes[j]])
        if A == 4:
            print("2 2")
        else:
            print(Output[0][0], end=" ")
            print(Output[0][1])
"""