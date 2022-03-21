"""
Date :- 4/7/21
Source :- https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

1921. Eliminate Maximum Number of Monsters
Medium

68

17

Add to List

Share
You are playing a video game where you are defending your city from a group of n monsters. 
You are given a 0-indexed integer array dist of size n, where dist[i] is the 
initial distance in meters of the ith monster from the city.

The monsters walk toward the city at a constant speed. The speed of each monster is 
given to you in an integer array speed of size n, where speed[i] is the speed of 
the ith monster in meters per minute.

The monsters start moving at minute 0. You have a weapon that you can choose to use 
at the start of every minute, including minute 0. You cannot use the weapon 
in the middle of a minute. The weapon can eliminate any monster that is still 
alive. You lose when any monster reaches your city. If a monster reaches 
the city exactly at the start of a minute, it counts as a loss, and the game ends 
before you can use your weapon in that minute.

Return the maximum number of monsters that you can eliminate before you lose, or 
n if you can eliminate all the monsters before they reach the city.

 

Example 1:

Input: dist = [1,3,4], speed = [1,1,1]
Output: 3
Explanation:
At the start of minute 0, the distances of the monsters are [1,3,4], you eliminate the first monster.
At the start of minute 1, the distances of the monsters are [X,2,3], you don't do anything.
At the start of minute 2, the distances of the monsters are [X,1,2], you eliminate the second monster.
At the start of minute 3, the distances of the monsters are [X,X,1], you eliminate the third monster.
All 3 monsters can be eliminated.
Example 2:

Input: dist = [1,1,2,3], speed = [1,1,1,1]
Output: 1
Explanation:
At the start of minute 0, the distances of the monsters are [1,1,2,3], you eliminate the first monster.
At the start of minute 1, the distances of the monsters are [X,0,1,2], so you lose.
You can only eliminate 1 monster.
Example 3:

Input: dist = [3,2,4], speed = [5,3,2]
Output: 1
Explanation:
At the start of minute 0, the distances of the monsters are [3,2,4], you eliminate the first monster.
At the start of minute 1, the distances of the monsters are [X,0,2], so you lose.
You can only eliminate 1 monster.
 

Constraints:

n == dist.length == speed.length
1 <= n <= 10^5
1 <= dist[i], speed[i] <= 10^5

"""

# Solution
"""

basic idea first we see at what time monster comes to reach us
then for example monster comes at 1 2 3 4 sec then we can kill all
but monsters comes at 2 2 2 seconds to uss then we can kill at max 2
prev is a time counter if times == monster coming time then monster will kill us
for example monster coming time is 1 2 3 3 then at t=0 we kill 1 st monster then prev becomes 1 then we kill monster who would have reached at 2 seconf then prev becomes 2 then we kill the monster who would have reached at 3 and prev becomes 3 but now one monster reached us game over
we used sort of times monster reach us
also we used count to see how many monsters we can kill

"""
import math
class Solution:
    def eliminateMaximum(self, dist: list[int], speed: list[int]) -> int:
        if 0 in dist:
            return 0
        time=[]
        for i in range(len(dict)):
            time.append(math.ceil(dist[i]/speed[i]))
        time.sort()
        kills=  0
        for i in range(len(time)):
            if i==time[i]:
                return kills
            else:
                kills += 1
        return kills
