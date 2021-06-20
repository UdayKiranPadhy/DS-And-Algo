"""

Source :-Edyst
Date :- 15/06/21

Particle Simulation
We are given an array of particles. Each particle has a positive size (greater than 0).

Any 2 particles can combine and produce a new particle, whose size is the absolute difference of the combined particles (possible 0). The old particles which combined have now vanished (because they combined).

This new particle can combine with any other particles. If particles are allowed to combine in any way, what is the minimum particle obtainable?

Note that combined particle size can never be lesser than 0.

Input format
The first line contains T, the number of test cases
Each test case contains first the size of the array n
This is followed by n numbers of the array, space-separated
Output
For each array, output the size of the minimum particle size possible
Constraints
2 <= n <= 100
1 <= A[i] <= 104
Example Input
4
5
30 27 26 10 6
4
1 2 4 8
4 
101 40 75 30
4
1 2 3 4
Output
0
1
4
0
Explanation
30,26 combine to give 4, the new array is : 4 27 10 6
Then 10,6 combine to give 4, the new array is: 4 27 4
Finally, 4,4 combine to give us 0
No matter how they combine, 1 is the minimum particle we can get
101,75 --> 26. Then 30,26 --> 4
4,3 --> 1. Then 1,1

"""


from functools import lru_cache
import sys


@lru_cache(None)
def go(li, t):
    if len(li) == 1:
        return li[0]
    mini = min(li)
    for i in range(len(li)):
        mini = min(mini,)
        pass


T = int(input())
for t in range(T):
    N = int(input())
    nums = [int(x) for x in input().strip().split(" ")]
    nums = tuple(nums)
    go(nums, t)
