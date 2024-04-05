"""

1023. Camelcase Matching
Medium

450

192

Add to List

Share Given an array of strings queries and a string pattern, return a boolean array answer where answer[i] is true
if queries[i] matches pattern, and false otherwise.

A query word queries[i] matches pattern if you can insert lowercase English letters pattern so that it equals the
query. You may insert each character at any position and you may not insert any characters.

 

Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: "FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: "FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: "FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
 

Constraints:

1 <= pattern.length, queries.length <= 100
1 <= queries[i].length <= 100
queries[i] and pattern consist of English letters.


"""

from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def go(word, pattern):
            if word == "" and pattern != "":
                return False
            elif word == "" and pattern == "":
                return True
            elif pattern != "" and word[0] == pattern[0]:
                return go(word[1:], pattern[1:])
            elif word[0].isupper():
                return False
            else:
                return go(word[1:], pattern)

        ans = []
        for word in queries:
            ans.append(go(word, pattern))
        return ans


model = Solution()
model.camelMatch(["FooBar", "FooBarTest", "FootBall",
                 "FrameBuffer", "ForceFeedBack"], "FB")
