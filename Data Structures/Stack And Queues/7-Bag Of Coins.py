"""
Problem Statement : HackWithInfy 2021

You are given n coin bags. Each coin bag has some coins in it and you
are allowed to take some coins. However, taking coins is not that
simple .
You have to choose a range [l, r] and an integer x which is less than or
equal to the number of coins in all the bags from range l to r. You can
take x coins from each of the bags in the range.

If you can do this only once, what is the maximum number of coins that
you can be obtained if you choose l, r and x optimally?

Input Format
The first line contains an integer, N, denoting the number of coin bags.
Each line i of the N subsequent lines (where 0 <= i < N) contains an
integer describing the number of coins in the coin bag

Constraints
1 <= N <= 10^4
1 <= am[i] <= 10^4


Sample Input 1:
4
1 2 3 4
Output:
6

Explanation:
The array is (1, 2, 3, 4). You can choose the range (2, 4) and x = 2 or
choose the range (3, 4) and x = 3. In
both ways you can
pick 6 coins.

Sample Input 2
5
4 3 3 4 4
Output:
15

Explanation:
The array is [4, 3, 3, 4, 4] You can
choose the range (1, 5) and x = 3,
pick 3 from all the bags in the range
to get 15 coins.

Sample Input 3:
Input:
6
1 2 2 3 2 3
Output :
10
Explanation:
The array is [1, 2, 2, 3, 2, 3]. You can
choose the range [2, 6] and x = 2,
pick 2 from all the bags in the range
to get 10 coins.

"""


def MAH(bags, b):
    left_smaller = b
    for i in R(b, -1, -1):
        if bags[i] < bags[b]:
            left_smaller = i
            break
    right_smaller = b
    for i in R(b, len(bags)):
        if bags[i] < bags[b]:
            right_smaller = i
            break
    return (right_smaller-(left_smaller+1))*bags[b]


def solve():
    n = I(input())
    bags = listInput()
    bags.insert(0, -1)
    bags.append(-1)
    coins = []
    for b in R(1, len(bags)-1):
        coins.append(MAH(bags, b))
    return max(coins)


if __name__ == '__main__':
    R = range
    I = int
    def listInput(): return [I(x) for x in input().strip().split(" ")]
    mod = 10000007
    inf = float('inf')
    for t in R(I(input())):
        print(solve())
