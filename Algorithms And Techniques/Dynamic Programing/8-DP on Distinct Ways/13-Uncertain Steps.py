"""

Uncertain Steps
Codu is trying to go down stairs from his building to ground floor.

He can go 3 ways:

Walk 1 step at a time.
Extend his legs and go 2 steps at a time.
Jump down 3 steps at a time.
Given n steps, calculate the number of possible ways to reach the ground floor, provided he can jump 3 steps at most once during this process.

That is, he can jump down 3 steps only once, but at any time, if he wishes, while walking down the stairs.

Constraints
1 <= N <= 1000000.
Input Format
Single Integer denoting the number of Steps, N
Output
Number of ways to reach ground floor.
As the number can be huge, give output modulo 1000000007.
Example Input 1
4
Output
7
Explanation
1, 1, 1, 1
1, 2, 1
1, 1, 2
1, 3
2, 1, 1
2, 2
3, 1
Number of ways = 7.

"""

def count_ways(n):
    if n == 1:
        return 1
    if n == 2 :
        return 2
    if n == 3:
        return 4
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)

n = int(input())
print(count_ways(n))