"""

https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/description/

Given a rectangular cake with height h and width w, and two arrays of integers 
horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the 
top of the rectangular cake to the ith horizontal cut and similarly, 
verticalCuts[j] is the distance from the left of the rectangular cake to the 
jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and 
vertical position provided in the arrays horizontalCuts and verticalCuts. Since 
the answer can be a huge number, return this modulo 10^9 + 7.

Example 1:

Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines 
are the horizontal and vertical cuts. After you cut the cake, the green piece of 
cake has the maximum area.

Example 2:

Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red 
lines are the horizontal and vertical cuts. After you cut the cake, the 
green and yellow pieces of cake have the maximum area.

Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
 

Constraints:

2 <= h, w <= 10^9
1 <= horizontalCuts.length < min(h, 10^5)
1 <= verticalCuts.length < min(w, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
It is guaranteed that all elements in horizontalCuts are distinct.
It is guaranteed that all elements in verticalCuts are distinct.

   Hide Hint #1  
Sort the arrays, then compute the maximum difference between two consecutive 
elements for horizontal cuts and vertical cuts.
   Hide Hint #2  
The answer is the product of these maximum values in horizontal cuts and vertical cuts.

"""


import sys

class Solution:
    def maxArea(self, h: int, w: int, hc: list[int], vc: list[int]) -> int:
        hc.append(0)
        hc.append(h)
        hc.sort()
        vc.append(0)
        vc.append(w)
        vc.sort()
        max_gap_horigontal=-sys.maxsize
        max_gap_vertical = -sys.maxsize
        for i in range(len(hc)-1):
            gap = hc[i+1] - hc[i]
            if gap > max_gap_horigontal:
                max_gap_horigontal = gap
        for i in range(len(vc)-1):
            gap = vc[i+1] - vc[i]
            if gap > max_gap_vertical:
                max_gap_vertical = gap
        return (max_gap_vertical * max_gap_horigontal)% 1000000007

model = Solution()
h,w = [int(x) for x in input().split(" ")]
hc = [int(x) for x in input().split(" ")]
vc = [int(x) for x in input().split(" ")]
print(model.maxArea(h,w,hc,vc))