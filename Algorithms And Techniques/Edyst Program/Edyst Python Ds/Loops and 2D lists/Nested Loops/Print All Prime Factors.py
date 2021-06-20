"""
Print all the prime factors
Complete the given method solve that takes as parameter a positive integer n and prints all the prime factors of the number n.

2 has only 1 prime factor: 2. However, for 63 there are 3 3 7

Note : Number will always greater than 1

Example Input: 6
Output: 2 3
Example Input: 27
Output: 3 3 3
Example Input: 321
Output: 3 107
"""


import math


def isPrime(n):
    if (n == 2) or (n == 3):
        return True
    if (n % 6 == 1) or (n % 6 == 5):
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True
    return False


def solve(n):
    for i in range(2, int(n / 2) + 1):
        if isPrime(i) and n % i == 0:
            while n % i == 0:
                n = n / i
                print(i, end=" ")


solve(27)