"""
Print the nth prime number
Complete the given method solve that takes as parameter an integer n and prints the nth prime number.

Example, the first prime number is 2. The next prime number: 3. The 7th prime number is 17

Example Input: 1
Output: 2
Example Input: 3
Output: 5
Example Input: 7
Output: 17
"""
import math


def solve(n):
    count = 0
    i = 1
    while count <= n:
        if isPrime(i):
            count += 1
        i += 1
    print(i - 1)


def isPrime(n):
    if (n == 2) or (n == 3):
        return True
    if (n % 6 == 1) or (n % 6 == 5):
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True
    return False


solve(7)