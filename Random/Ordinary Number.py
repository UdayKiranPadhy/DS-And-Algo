"""

B. Ordinary Numbers
time limit per test:2 seconds
memory limit per test:256 megabytes
inputstandard input
outputstandard output
Let's call a positive integer n ordinary if in the decimal notation all its digits are 
the same. For example, 1, 2 and 99 are ordinary numbers, but 719 and 2021 are not 
ordinary numbers.

For a given number n, find the number of ordinary numbers among the numbers from 1 to n.

Input
The first line contains one integer t (1≤t≤10^4). Then t test cases follow.

Each test case is characterized by one integer n (1≤n≤10^9).

Output
For each test case output the number of ordinary numbers among numbers from 1 to n.

Example
inputCopy
6
1
2
3
4
5
100
outputCopy
1
2
3
4
5
18
"""

# Solution
# Note that every ordinary number can be represented as d⋅(10^0+10^1+…+10^k). Therefore,
# to count all ordinary numbers among the numbers from 1 to n, it is enough to count
# the number of (d,k) pairs such that d⋅(100+101+…+10k)≤n. In the given constraints, it
# is enough to iterate over d from 1 to 9 and k from 0 to 8.


def solve():
    n = I(input())
    if n == 1:
        print(1)
        return
    count = 0
    for d in range(1, 10):
        multipler = 0
        for k in range(0, 10):
            multipler = multipler + pow(10, k)
            if d * multipler <= n:
                count += 1
    print(count)


if __name__ == "__main__":
    I = int
    R = range
    for i in range(int(input().strip())):
        solve()
