"""
CountPaths
Find the number of ways to reach e from s.
No of steps which can be taken = 1,2,3,4,5,6

Sample Input:
4
Sample Output:
4

Explanation:
1 2 3 4
1= 1 2 3 4
2=1 2 4
3=1 3 4
4=1 4
"""

def steps(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    count = 0
    for i in range(1,6):
        count += steps(start + i, end)
    return count


def steps2(start, end):
    if start == end:
        return 1
    if start > end:
        return 0
    count =  steps2(start + 1, end) + steps2(start + 2, end) + steps2(start + 3, end) + steps2(start + 4, end)
    return count


print(steps(1, 4))

"""
Time Complexity:O(2^n)
Space Complexity : O(2^n)
"""