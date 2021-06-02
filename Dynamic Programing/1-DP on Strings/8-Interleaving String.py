"""
Interleaving Strings
Medium

Given strings s1, s2, and s3, find whether s3 is formed by an 
interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where 
they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true

Constraints:
0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
 

Follow up: Could you solve it using only O(s2.length) additional memory space?

"""

# My Initial Trails Failed no need to check


# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         if len(s1) + len(s2) != len(s3):
#             return False
#         iterator1 = 0
#         iterator2 = 0
#         iterator3 = 0
#         while iterator1 + iterator2 != len(s3):
#             if s2[iterator2] == s3[iterator3]:
#                 iterator2 += 1
#                 iterator3 += 1
#             elif s1[iterator1] == s3[iterator3]:
#                 iterator1 += 1
#                 iterator3 += 1
#             else:
#                 return False
#         return True


# My Trails Passed (Happy)
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache(None)
        def dynamic(i, j, k):
            if i == len(s1):
                if s2[j:] == s3[k:]:
                    return True
                else:
                    return False
            elif j == len(s2):
                if s1[i:] == s3[k:]:
                    return True
                else:
                    return False
            elif s1[i] == s2[j] and s2[j] == s3[k]:
                return dynamic(i+1, j, k+1) or dynamic(i, j+1, k+1)
            elif s1[i] == s3[k]:
                return dynamic(i+1, j, k+1)
            elif s2[j] == s3[k]:
                return dynamic(i, j+1, k+1)
            else:
                return False

        return dynamic(0, 0, 0)

model = Solution()
s1 = input()
s2 = input()
s3 = input()
print(model.isInterleave(s1, s2, s3))
