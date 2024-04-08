"""
https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/description/

1497. Check If Array Pairs Are Divisible by k
Medium

Given an array of integers arr of even length n and an integer k.

We want to divide the array into exactly n / 2 pairs such that the sum of each pair is 
divisible by k.

Return True If you can find a way to do that or False otherwise.

 

Example 1:

Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:

Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:

Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
Example 4:

Input: arr = [-10,10], k = 2
Output: true
Example 5:

Input: arr = [-1,1,-2,2,-3,3,-4,4], k = 3
Output: true
 

Constraints:

arr.length == n
1 <= n <= 105
n is even.
-109 <= arr[i] <= 109
1 <= k <= 105



"""

# Algorithm
# Keep an array of the frequencies of ((x % k) + k) % k for each x in arr.
# for each i in [0, k - 1] we need to check if freq[k] == freq[k - i]
# Take care of the case when i == k - i and when i == 0

from collections import Counter


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        gg = [((i % k)+k) % k for i in arr]
        gg = Counter(gg)
        for i in gg.keys():
            if gg[i] == gg[k-i]:
                continue
            elif i == 0:
                if gg[i] % 2 == 0:
                    continue
                else:
                    return False
            else:
                return False
        return True
