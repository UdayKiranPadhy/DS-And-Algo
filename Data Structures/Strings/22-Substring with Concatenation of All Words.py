"""

Substring with Concatenation of All Words
Hard

1452

1603

Add to List

Share
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

"wordgoodgoodgoodbestword"
["word","good","best","good"]
[8]

Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.

"""


# Problem statement
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

# Solution
# The idea is the following: first, we can divide this problem into several sub-problems,
# because all words have the same length, barfoothefoobarman is divided into
# groups{bar, foo, the, foo, bar, man}, {arf, oot, hef, oob, arm} and {rfo, oth, efo, oba, rma}
# and then problem is similar to 0438, where we need to find anagram substring. We use dictionary
# with words and number of occurrences and use sliding window technique, keeping number of correct
# values.

# Complexity
# Overall complexity of this algorithm is O(nk), where n is size of original string and k is the
# length of each word. Memory is O(n): on each group we need to keep no more that one copy of
# string.

from collections import Counter


class Solution:
    def findSubstring(self, s, words):
        n, k, m = len(s), len(words), len(words[0])
        ans = []

        for j in range(m):
            d1, d2 = Counter(words), Counter()

            num_to_correct = len(d1)
            for i in range(j, n, m):
                new_s = s[i:i+m]
                d2[new_s] += 1
                if d1[new_s] == d2[new_s]:
                    num_to_correct -= 1
                if d2[new_s] == d1[new_s] + 1:
                    num_to_correct += 1

                if i - m*k >= 0:
                    old_s = s[i-m*k:i-m*k+m]
                    d2[old_s] -= 1
                    if d2[old_s] == d1[old_s] - 1:
                        num_to_correct += 1
                    if d1[old_s] == d2[old_s]:
                        num_to_correct -= 1

                if num_to_correct == 0:
                    ans.append(i+m-m*k)

        return ans


# My Solution
# Rolling Hash similar to previous one but slight variation


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if len(words) == 0:
            return []
        window = len(words[0])
        N = len(s)
        no_of_words = len(words)
        ans = set()
        for i in range(window):
            for j in range(i, N-no_of_words*window+1):
                d1 = Counter(words)
                for k in range(j, j + (no_of_words*window), window):
                    if s[k:k+window] in d1:
                        if d1[s[k:k+window]] > 0:
                            d1[s[k:k+window]] -= 1
                        else:
                            break
                    else:
                        break

                if list(d1.values()) == [0] * len(d1):
                    ans.add(j)
        return list(ans)


model = Solution()
print(model.findSubstring("wordgoodgoodgoodbestword",
      ["word", "good", "best", "good"]))
