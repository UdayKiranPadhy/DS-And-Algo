import sys
import math
import string

digs = string.digits + string.ascii_letters


def isPrime(n):
    if (n == 2) or (n == 3):
        return True
    if (n % 6 == 1) or (n % 6 == 5):
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True
    return False


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[int(x % base)])
        x = int(x / base)
    if sign < 0:
        digits.append("-")
    digits.reverse()
    return "".join(digits).upper()


def isBase(num, base):
    v = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 18,
        "J": 19,
        "K": 20,
        "L": 21,
        "M": 22,
        "N": 23,
        "O": 24,
        "P": 25,
        "Q": 26,
        "R": 27,
        "S": 28,
        "T": 29,
        "U": 30,
        "V": 31,
        "W": 32,
        "X": 33,
        "Y": 34,
        "Z": 35,
    }
    bases = -sys.maxsize - 1
    for j in str(num):
        if bases < v[j]:
            bases = v[j]
    if bases + 1 == base:
        return True
    return False


l = []
for i in range(int(input())):
    l.append(input().split())

v = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
    "H": 17,
    "I": 18,
    "J": 19,
    "K": 20,
    "L": 21,
    "M": 22,
    "N": 23,
    "O": 24,
    "P": 25,
    "Q": 26,
    "R": 27,
    "S": 28,
    "T": 29,
    "U": 30,
    "V": 31,
    "W": 32,
    "X": 33,
    "Y": 34,
    "Z": 35,
}
for i in l:
    base = -sys.maxsize - 1
    value = 0
    for j in i[0]:
        if base < v[j]:
            base = v[j]
    power = len(i[0]) - 1
    for j in i[0]:
        value += v[j] * ((base + 1) ** power)
        power -= 1
    for j in range(value + 1, sys.maxsize):
        if isPrime(j):
            if isBase(int2base(j, v[i[1]] + 1), v[i[1]] + 1):
                print(int2base(j, v[i[1]] + 1))
                break