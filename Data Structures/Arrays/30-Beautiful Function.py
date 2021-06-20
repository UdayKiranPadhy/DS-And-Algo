"""
Source :- HackWithInfy
Date :- 15/06/2021

Beautiful Function
Let's define a Beautiful Function F(x) in such a way: Add 1 to the value of. I fht result of addition contains any trailing zeros, then remove them all.

Example

F(11) = F(12)

F(19) = 2 (20 -> 2)

F(99) = 1 (100 -> 10 -> 1)

Let's define a number to be reachable from x, if we can apply the Beautiful Function some number of times (possibly zero) to x and get that number as result.

Ex. 102 is reachable from 10099 as F(F(10099))) = F(101) = 102

You are given a number N. Calculate how many numbers are reachable from N.

Input format
The first line contains an integer N, denoting the given number.

Constraints
1 <= N <= 109

Sample Input
1
Sample Output
9
Explanation
1,2,3,4,5,6,7,8,9 are reachable from 1

"""

visited = set()


def F(n):
    if (n+1) % 10 == 0:
        n = n+1
        n = str(n)
        n = n.rstrip("0")
        return int(n)
    else:
        return n+1


n = int(input())
while True:
    if n in visited:
        break
    else:
        visited.add(n)
    n = F(n)
print(len(visited))
