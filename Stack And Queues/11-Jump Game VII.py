"""
Problem Statement :- https://leetcode.com/problems/jump-game-vii/
1871. Jump Game VII
Medium

You are given a 0-indexed binary string s and two integers minJump and maxJump. 
In the beginning, you are standing at index 0, which is equal to '0'. You can 
move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.
 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.


Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
 

Constraints:
2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length

"""


# Solution
"""
See what we are doing is, from curr_index we can go to 
[curr_index + minJumps, curr_index + maxJump] indices

we will make a queue where we will keep indices where we have jumped from some other 
position, and we will jump from them after some time
initially there will be 0 in queue, as we have to start from there we will put the 
indices of range where we can reach from 0 in queue

let us assume at any state in between, we had 3 in our queue as front element
if we are at index 3 now, (let minJ = 2, maxJ = 4) then I can go from 
[3+2, 3+4] = [5, 7] indices, so we will put all of them in queue

now let's assume next index is 4 in queue
for 4 the new indices rechable from here are [4+2, 4+4] = [6, 8], but we already 
inserted indices from 5 to 6 using index 3, so why to put them again, if we do this 
it will be simple approach but will lead to O(n * jump_size) run time

so instead of pushing [curr_index + minJumps, curr_index + maxJump] range in queue, 
we can push [max(curr_index + minJumps, max_till_now + 1), curr_index + maxJump]
so here max_till_now would have helped us to skip indices 5 to 6 from again inserting in queue.

"""


# Mytrails Didnt succed due to TLE go down for success solution




import collections
from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] != '0':
            return False

        q, farthest = deque([0]), 0

        while(len(q) != 0):
            element = q.popleft()
            if element == len(s)-1:
                return True
            for i in range(element+minJump, element+maxJump+1):
                if i >= len(s):
                    continue
                elif s[i] == '0':
                    if i > farthest:
                        q.append(i)
                        farthest = i
        else:
            return False


model = Solution()
print(model.canReach("01101110", 2, 3))
print(model.canReach("011010", 2, 3))


# Accepted once


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = collections.deque([0])
        mx = 0
        while queue:
            i = queue.popleft()
            for j in range(max(i + minJump, mx + 1), min(i + maxJump + 1, len(s))):
                if s[j] == '0':
                    if j == len(s) - 1:
                        return True
                    queue.append(j)
                mx = i + maxJump
        return False
