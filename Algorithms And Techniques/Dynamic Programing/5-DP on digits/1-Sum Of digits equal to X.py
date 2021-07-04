"""

Given an integer Y and a range [L, R], the task is to find the count of 
all numbers from the given range whose sum of digits is equal to Y.
Examples: 
 

Input: L = 0, R = 11, Y = 2 
Output: 2 
2 -> 2 
11 -> 1 + 1 = 2
Input: L = 500, R = 1000, Y = 6 
Output: 3 
 
https://www.geeksforgeeks.org/count-of-numbers-from-range-l-r-whose-sum-of-digits-is-y/

https://youtu.be/2yAEj-0A8bk

https://codeforces.com/blog/entry/53960

https://leetcode.com/problems/numbers-at-most-n-given-digit-set/discuss/559624/python-digit-dp
"""

Y = 5
# dp = [[[0 for i in range(18 + 1)] for j in range(18 * 9 + 1)] for k in range(2)]

answer = 0
l = []


def Count(num, n, sum, tight):
    global string2
    global Y
    global answer
    if sum == Y:
        print(l)
        answer += 1
        return 1
    elif n >= len(str(num)):
        return 0
    elif sum > Y:
        return 0
    upper_bound = 9 if not tight else int(str(num)[n])
    for i in range(0, upper_bound + 1):
        l.append(i)
        Count(num, n + 1, sum + i, (tight and (i == upper_bound)))
        l.pop()
    return answer

print(Count(15, 0, 0, 1))