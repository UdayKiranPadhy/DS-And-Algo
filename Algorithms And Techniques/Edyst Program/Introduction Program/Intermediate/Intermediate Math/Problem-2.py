# This is perfect

"""
Write a program to determine whether a number N is equal to the sum of its proper positive divisors (excluding the number itself).

Input format

First line: T (number of test cases)
For each test case
First line: N
Output format

Print YES, if N is equal to the sum of its proper positive divisors else print NO.

Constraints

1 ≤ T ≤ 100
1 ≤ N ≤ 109

Sample Input

3
6
5
28
Sample Output

YES
NO
YES
Explanation

6 = 1 + 2+ 3, so it is perfect.

5 != 1 , so it is not perfect.

28 = 1 + 2 + 4 + 7 + 14, so it is perfect.
"""

# solution
"""
def factor(i, n):
    if n % i == 0:
        return True
    return False


def sum(l):
    count = 0
    for i in l:
        count += i
    return count


t = int(input())
for i in range(t):
    l.append(int(input()))
for i in l:
    factors = []
    for j in range(1, i):
        if factor(j, i):
            factors.append(j)
    sumi = sum(factors)
    if sumi == i:
        print("YES")
    else:
        print("NO")
"""
# This solution is ok But time limit exceeds the limits

t = int(input())
l = []
for i in range(t):
    l.append(int(input()))
maxi = max(l)
# initialize - all entries are multiples of 1
#   (ignore sieve[0] and sieve[1])
sieve = [1] * (maxi + 1)
Output = []
n = 2
while n <= maxi:
    if sieve[n] == n:
        Output.append(n)

    kn = 2 * n
    while kn <= maxi:
        sieve[kn] += n
        kn += n

    n += 1
for i in l:
    if i in Output:
        print("YES")
    else:
        print("NO")


"""
n=int(input())
for i in range(n):
    i=int(input())
    m={1}
    if i==1:
        print("NO")
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            m.add(j)
            m.add(i//j)
    if sum(m)==i:
        print("YES")
    else:
        print("NO")
"""