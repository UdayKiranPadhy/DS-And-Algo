"""
Source :- Edyst
Date :- 12/06/21

Removing chocolates
A box contains a number of chocolates that can only be removed 1 at a time or 3 at a a time. How many ways can the box be emptied?

The answer can be very large so return it modulo of 10^9+7

For example, there are n = 7 chocolates initially. They can be removed nine ways as follows:

(1,1,1,1,1,1,1)
(1,1,1,1,3)
(1,1,1,3,1)
(1,1,3,1,1)
(1,3,1,1,1)
(3,1,1,1,1)
(1,3,3)
(3,1,3)
(3,3,1)
Input format: Single line represents the no of chocolates in the box.

Output format: The number of ways of removing the chocolates modulo 10^9 + 7

Constraints:

1 <= n <= 10^9
Sample Input 1 :

1
Sample Output 1 :

1
Explanation:: There is only one way to remove a chocolate, so

ans = 1 % 1000000007 = 1
Sample Input 2 :

3
Sample Output 2 :

2
Explanation: There are two ways to remove all the chocolates.

remove all 3 at once,
remove one after the other, so
ans = 2 % 1000000007 = 2.

"""

"""
from functools import lru_cache
import sys
 
# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs
 
sys.setrecursionlimit((10**9)+2)


@lru_cache(None)
def count_ways(n):
    if n == 1:
        return 1
    if n== 2:
        return 1
    if n == 3:
        return 2
    else:
        return count_ways(n-3)%1000000007 + count_ways(n-1)%1000000007


n = int(input())
print(count_ways(n)%1000000007)

"""


def count_ways(n):
    vals = [0]*(n+1)
    if n == 1 or n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        vals[1] = 1
        vals[2] = 1
        vals[3] = 2
        for i in range(4, n + 1):
            vals[i] = vals[i-1] + vals[i-3]
        return vals[n]


n = int(input())

gg = count_ways(n) % 1000000007
print(gg)

"""
n = int(input())
m = 1000000007
l = [1,1,2]
for i in range(3,n):
    l.append(l[i-1]%m+l[i-3]%m)
print(l[n-1]%m)
"""






