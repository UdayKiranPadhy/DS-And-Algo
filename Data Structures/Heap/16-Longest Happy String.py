"""

1405. Longest Happy String
Medium

1003

171

Add to List

Share
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0

Use a greedy approach.

Use the letter with the maximum current limit that can be added without breaking the condition.

"""

import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res , maxHeap = "" , []
        for count , alpha in [(-a,"a"),(-b,"b"),(-c,"c")]:
            if count:
                heapq.heappush(maxHeap,(count,alpha))
        
        while maxHeap:
            count , alpha = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == alpha:
                if maxHeap:
                    count2 , alpha2 = heapq.heappop(maxHeap)
                    res += alpha2
                    count2 += 1
                    if count2 :
                        heapq.heappush(maxHeap,(count2,alpha2))
                    heapq.heappush(maxHeap,(count,alpha))
                else:
                    break
                pass
            else:
                count += 1
                res += alpha
                if count :
                    heapq.heappush(maxHeap,(count,alpha))
        return res