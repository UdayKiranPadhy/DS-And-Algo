"""


14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

"""

# We can do it very simply by a cool and powerful technique called "Reduction".

# Basically we compare the two strings from the list and get one longest sub_string
# from them, we compare this sub_string and the next element.We get another longest
# sub_string from this and we compare it with the next element. We continue this
# until we reach the end of the list. This is called Reduction technique and is a
# very powerful technique. I encourage you to read more about this.

# Complexity for the loop 1 will be O(m) where m=min(len(str1),str(2))
# Complexity for loop 2 will be O(n) as we are comparing all the elements in the
# loop once except string1.
# So complexity is O(mn)

# Solution 1:


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        def compare(first: str, sec: str) -> str:  # we use this to compare two strings
            # determine the min length between the two strings
            l = min(len(first), len(sec))
            sub = ""  # this is the sub string that will be our result of the comparion
            # We compare each element for string1 and string2 present at the same index like this: first[0],sec[0] ; first[1], sec[1]
            # nd so on till the length of shorter string. When they are no more equal, we break out of the loop.
            for i in range(l):
                if first[i] == sec[i]:
                    sub += sec[i]
                else:
                    break
            return sub

        # this is for the first time when we want to compare string1 and string2 and take the result and compare with string3
            # and so on.
            # We want to generalise this as well so we take sub_string of string1 and string1 and get the result which is also string1 and compare it with string2.
            # In this way we don't have to get the sub_string from the first two strings separately
        sub = strs[0]
        for w in range(1, len(strs)):
            sub = compare(sub, strs[w])
        return sub
# Solution 2: Here we use a very cool and built in Pyhton function called zip.
# Its internal mechanism and simplified version has been described in solution 1.


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        def compare(first: str, sec: str) -> str:
            sub = ""
            # zip function compares the two characters present at the same index for two strings like first[0],sec[0] ; first[1],sec[1] until any of the string ends
            for i, j in zip(first, sec):
                if i != j:
                    break
                sub += i
            return sub

            # rest is same as the previous solution
        long_sub = strs[0]
        for w in range(1, len(strs)):
            long_sub = compare(long_sub, strs[w])
        return long_sub

# My Initial Approach


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        # Calculate the minimum length string from the strs
        min_length = 10**6
        for i in strs:
            min_length = min(min_length, len(i))

        length = 0
        comefrombreak = False
        for i in range(min_length):
            to_find = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] == to_find:
                    continue
                else:
                    comefrombreak = True
                    break
            if comefrombreak:
                break
            else:
                length += 1
        return strs[0][:length]
