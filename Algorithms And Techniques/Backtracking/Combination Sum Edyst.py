"""
Date :- 21/06/21
Source :- Edyst

Combination Sum
Given an array of distinct integers arr and a target integer target, return a list of all unique combinations of arr where the chosen numbers sum to target.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.


Note:

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR … (a1 = b1 AND a2 = b2 AND … ai = bi AND ai+1 > bi+1)
The solution set must not contain duplicate combinations
Input Format

The first line contains N, denoting the size of the array.

The second line contains N spaced separated integers, denoting the elements of array.

The third line contains the the target value.

Example Input 1

4
7 2 6 5
16
Example Output 1:

2 2 2 2 2 2 2 2
2 2 2 2 2 6
2 2 2 5 5
2 2 5 7
2 2 6 6
2 7 7
5 5 6
Your Answer

"""

n = int(input())
arr = [int(x) for x in input().split(" ")]
target = int(input())
arr = list(set(arr))
arr.sort()
solutions = []


def backtrack(index, upto_now, sum):
    if sum == target:
        solutions.append(upto_now[:])
        return
    if sum > target:
        return
    if index >= len(arr):
        return
    for i in range(index, len(arr)):
        upto_now.append(arr[i])
        backtrack(i, upto_now, sum+arr[i])
        upto_now.pop()


upto_now = []
backtrack(0, upto_now, 0)
for i in solutions:
    print(*i)
