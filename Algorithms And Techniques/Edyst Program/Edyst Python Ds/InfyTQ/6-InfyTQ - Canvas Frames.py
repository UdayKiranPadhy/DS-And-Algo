"""
Given n sticks whose lengths equal a1, a2, ... an.

And you want to make a h × w-sized frame, to make a frame you needs two sticks whose lengths equal h and two sticks whose lengths equal w. Specifically, to make a square frame (when h = w), you needs four sticks of the same length.

You cannot break the sticks or glue them together.

You have to calculate, what is the maximum number of frames that can be made using the given sticks. It's not necessary to use all the sticks. The area of each frame doesn't matter. We want the most number for frames possible.

Note : It is not necessary to use all the sticks you have.

Input :
[2, 2, 3, 2, 3, 2]

Output :
1

Explanation :

Either you can make a frame of size 2x3 or 2x2 or 3x2 but you can make only one frame because after making a frame any of these size, there only 2 sticks left.
"""


class Solution:
    def makeFrames(self, A):
        c = 0
        skip = False
        A.sort()
        for i in range(len(A) - 1):
            if skip:
                skip = False
                continue
            if A[i] == A[i + 1]:
                skip = True
                c += 1
        return c // 2
