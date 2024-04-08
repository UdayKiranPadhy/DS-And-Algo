"""
https://leetcode.com/problems/combination-sum/description/

39. Combination Sum
Medium

Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen 
numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen 
numbers is different.

It is guaranteed that the number of unique combinations that sum up to target 
is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.


Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]


Example 3:

Input: candidates = [2], target = 1
Output: []


Example 4:

Input: candidates = [1], target = 1
Output: [[1]]


Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500

"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        output = []

        def backTrack(index, total, now):
            if total == target:
                output.append(now[:])
            for i in range(index, len(candidates)):
                if total + candidates[i] <= target:
                    now.append(candidates[i])
                    backTrack(i, total+candidates[i], now)
                    now.pop()
        gg = []
        backTrack(0, 0, gg)
        return output


# Dont search for time complexity
# It varies according to input
# SC would be O(T/M) T = target and M = min values in list
# TC would be O(k * 2^N) k is the average length of ans and N is the length of list
