"""
Problem Statement:-https://leetcode.com/problems/open-the-lock/

Open Lock
Medium

You have a lock in front of you with 4 circular wheels. Each wheel 
has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The 
wheels can rotate freely and wrap around: for example we can turn '9' to 
be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state 
of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays 
any of these codes, the wheels of the lock will stop turning and you 
will be unable to open it.

Given a target representing the value of the wheels that will unlock 
the lock, return the minimum total number of turns required to open 
the lock, or -1 if it is impossible.

 

Example 1:

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be 
"0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" 
would be invalid, because the wheels of the lock become stuck after 
the display becomes the dead end "0102".

Example 2:

Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".


Example 3:

Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.

Example 4:

Input: deadends = ["0000"], target = "8888"
Output: -1

Constraints:

1 <= deadends.length <= 500
deadends[i].length == 4
target.length == 4
target will not be in the list deadends.target and deadends[i] consist of digits only.
   

 Hint #1  
We can think of this problem as a shortest path problem on a graph: there 
are `10000` nodes (strings `'0000'` to `'9999'`), and there is an edge between 
two nodes if they differ in one digit, that digit differs by 1 
(wrapping around, so `'0'` and `'9'` differ by 1), and if *both* nodes are not 
in `deadends`.
"""


# Solution - I (BFS)
"""
First, let's simplify the problem statement. We are given a string start = "0000" 
and asked to reach target by turning (minimum times) a digit forward or backward 
one at a time without reaching any of the strings in deadends.

We can't just turn a digit forward or backward just based on which turn gets us 
quicker to the corresponding digit of target faster because this approach may 
lead us towards a deadend. So, it makes sense to try and turn a digit in both 
the direction and return the one that leads to target in minimum moves.

The solution can be modelled as a BFS traversal, wherein we try to shift each 
digit of current string curstr in both the possible direction. We increment turns 
at each level of BFS and return when target is reached during the traversal.

We use a hashset to insert all the deadends string for efficient check on whether 
we reach a deadend at anytime. Similarly, we store all the visited string in 
visited to ensure that we won't revisit a string again. For BFS traversal, we 
would also require to maintain a queue. The algorithm can be summed up into 
following steps:-

1)Insert all strings from deadends into a hashset and also maintain a 
visited set for all strings traversed so far.
2)Start BFS traversal from "0000" by pushing it into the queue and looping 
till the queue becomes empty.
3)At each level of BFS, take the current string and try turning each digit 
in both forward & backward direction. For eg. we can apply the turning 
process on "0000" to get ["1000", "9000", "0100", "0900", "0010", "0090", "0001", "0009"].
4)If any of the strings after applying turning process become equal to target, return the 
turns required till now.
5)Else, just push the turned strings into the queue, insert it into visited set and 
repeat the same process for all strings in the queue.
5)If the queue becomes empty, we have tried all possible paths to reach target and failed. 
So return -1.

"""


# My Trails Failed




from collections import deque
def turn(string, i):
    to_return = []
    if int(string[i])+1 > 9:
        to_return.append(string[:i]+"0"+string[i+1:])
        to_return.append(string[:i]+str(int(string[i])-1) + string[i+1:])
    elif int(string[i])-1 < 0:
        to_return.append(string[:i]+str(int(string[i])+1) + string[i+1:])
        to_return.append(string[:i]+"9"+string[i+1:])
    else:
        to_return.append(string[:i]+str(int(string[i])+1)+string[i+1:])
        to_return.append(string[:i]+str(int(string[i])-1)+string[i+1:])
    return to_return


class Solution(object):
    def OpenLock(self, deadends, target):
        deadends = set()
        if target in deadends:
            return -1
        visited = set()
        queue = deque()
        queue.append("0000")
        rotations = 0
        while len(queue) != 0:
            N = len(queue)
            for i in range(N):
                poppedString = queue.popleft()
                if poppedString not in visited and poppedString not in deadends:
                    visited.add(poppedString)
                    if poppedString == target:
                        return rotations
                    for i in range(4):
                        turned = turn(poppedString, i)
                        for _ in turned:
                            if (_ not in deadends) and (_ not in visited):
                                queue.append(_)
            rotations += 1
        else:
            return -1


# model = Solution()
# deadends = ["0000", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
# target = "8888"
# print(model.OpenLock(deadends, target))


# Solution Accepted

class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        def neighbors(code):
            for i in range(4):
                x = int(code[i])
                for diff in (-1, 1):
                    y = (x + diff + 10) % 10
                    yield code[:i] + str(y) + code[i + 1:]

        deadSet = set(deadends)
        if "0000" in deadSet:
            return -1
        q = deque(["0000"])
        steps = 0
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == target:
                    return steps
                for nei in neighbors(curr):
                    if nei in deadSet:
                        continue
                    deadSet.add(nei)  # Marked as visited
                    q.append(nei)
            steps += 1

        return -1
