"""

Date :- 3/7/21
Link :- https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/




1647. Minimum Deletions to Make Character Frequencies Unique
Medium

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

 

Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0 is ignored).
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
"""


class Solution:
    def minDeletions(self, s: str) -> int:
        alpha = {}
        for i in s:
            if i in alpha:
                alpha[i] += 1
            else:
                alpha[i] = 1
        count = 0
        values = list(alpha.values())
        dups = []
        unique = set()
        for i in values:
            if i not in unique:
                unique.add(i)
            else:
                dups.append(i)
        if dups == []:
            return count
        for i in dups:
            while i in unique:
                i -= 1
                count += 1
            if i != 0:
                unique.add(i)
        return count


class Solution:
    def minDeletions(self, s: str) -> int:
        frequency = collections.Counter(s)

        seen = set()
        res = 0

        for c, freq in frequency.items():
            while freq > 0 and freq in seen:
                freq -= 1
                res += 1
            seen.add(freq)
        return res

model = Solution()
print(model.minDeletions('aaabbbcc'))
