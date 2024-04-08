"""
https://leetcode.com/problems/print-words-vertically/description/
1324. Print Words Vertically
Medium

329

80

Add to List

Share
Given a string s. Return all the words vertically in the same order in which they 
appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. 
(Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there 
will be only one word.

 

Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"
Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
Example 3:

Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
 

Constraints:

1 <= s.length <= 200
s contains only upper case English letters.
It's guaranteed that there is only one space between 2 words.

"""

# Solution Approach
# 1)Seperate individual words based on spaces
# 2)Find the maximum length of the words present
# 3)Adjust spacing of every word according to the max length
# 4)Traverse each word max_length times


class Solution:
    def printVertically(self, s: str) -> list[str]:
        words = s.split()
        for i in range(len(words)):
            words[i] = words[i].strip()

        lenghts = [len(i) for i in words]
        max_length = max(lenghts)

        for i in range(len(words)):
            words[i] = words[i].ljust(max_length, " ")

        answer = []
        for i in range(max_length):
            word = ""
            for j in words:
                word = word + j[i]
            answer.append(word)

        # Strip all extra spaces
        for i in range(len(answer)):
            answer[i] = answer[i].rstrip()
        return answer


# In Short
def printVertically(self, s: str) -> List[str]:
    s = str.split(s)
    m = max([len(x) for x in s])
    ans = [""]*m
    for x in s:
        for i in range(m):
            if i >= len(x):
                ans[i] += " "
            else:
                ans[i] += x[i]
    return [x.rstrip() for x in ans] #rstrip() removes trailing spaces

model = Solution()
model.printVertically("Uday is my name")
