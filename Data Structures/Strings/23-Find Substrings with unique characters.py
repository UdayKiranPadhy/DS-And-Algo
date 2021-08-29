"""
Source : Impeatus Company Exam , On Campus by Akrithi

Count of substrings having all distinct characters

Given a string str consisting of lowercase alphabets, the task is to find the 
number of possible substrings (not necessarily distinct) that consists of 
distinct characters only.

Examples: 
Input: Str = “gffg” 
Output: 6 
Explanation: 
All possible substrings from the given string are, 
( “g“, “gf“, “gff”, “gffg”, “f“, “ff”, “ffg”, “f“, “fg“, “g” ) 
Among them, the highlighted ones consists of distinct characters only.

Input: str = “gfg” 
Output: 5 
Explanation: 
All possible substrings from the given string are, 
( “g“, “gf“, “gfg”, “f“, “fg“, “g” ) 
Among them, the highlighted consists of distinct characters only. 


"""
# Soultion:-
# https://www.geeksforgeeks.org/count-of-substrings-having-all-distinct-characters/

# Naive Approach:
# The simplest approach is to generate all possible substrings from the given
# string and check for each substring whether it contains all distinct
# characters or not. If the length of string is N, then there will
# be N*(N+1)/2 possible substrings.

# Time complexity: O(N^3)
# Auxiliary Space: O(1)

# Efficient Approach:
# The problem can be solved in linear time using Two Pointer Technique, with the
# help of counting frequencies of characters of the string.

# Detailed steps for this approach are as follows:

# 1)Consider two pointers i and j, initially both pointing to the first character
# of the string i.e. i = j = 0.
# 2)Initialize an array Cnt[ ] to store the count of characters in substring from
# index i to j both inclusive.
# 3)Now, keep on incrementing j pointer until some a repeated character is
# encountered. While incrementing j, add the count of all the substrings ending at jth
# index and starting at any index between i and j to the answer. All these substrings
# will contain distinct characters as no character is repeated in them.
# 4)If some repeated character is encountered in substring between index i to j, to
# exclude this repeated character, keep on incrementing the i pointer until repeated
# character is removed and keep updating Cnt[ ] array accordingly.
# 5)Continue this process until j reaches the end of string. Once the string is
# traversed completely, print the answer.

def findSubstrings(Str):
    n = len(Str)
    ans = 0
    cnt = 26 * [0]

    i, j = 0, 0

    while (i < n):
        if (j < n and
           (cnt[ord(Str[j]) - ord('a')] == 0)):
            cnt[ord(Str[j]) - ord('a')] += 1
            ans += (j - i + 1)
            j += 1
        else:
            cnt[ord(Str[i]) - ord('a')] -= 1
            i += 1
    return ans


gg = "bcada"
print(findSubstrings(gg))
