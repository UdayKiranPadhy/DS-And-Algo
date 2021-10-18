"""

648. Replace Words
Medium

https://leetcode.com/problems/replace-words/

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
Example 3:

Input: dictionary = ["a", "aa", "aaa", "aaaa"], sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
Output: "a a a a a a a a bbb baba a"
Example 4:

Input: dictionary = ["catt","cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 5:

Input: dictionary = ["ac","ab"], sentence = "it is abnormal that this solution is accepted"
Output: "it is ab that this solution is ac"
 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 10^6
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Each two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.

"""

# Problem statement
# https://leetcode.com/problems/replace-words/

# Solution
# Best complexity solution is to put all our dictionary to trie, then we just traverse
# our string and stop either when word is ended or we found ending node in our Trie.

# Complexity
# Time and space complexity will be O(m + n), where m is total length of all words in dictionary.

# Code


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):  # None
        node = self.root
        for symbol in word:
            node = node.children.setdefault(symbol, TrieNode())
        node.end_word = word

    def find(self, word):
        node = self.root
        for l in word:
            if l not in node.children or node.end_word:
                break
            node = node.children[l]
        return node.end_word if node.end_word else word


class Solution:
    def replaceWords(self, dictionary, sentence):
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        return " ".join(trie.find(word) for word in sentence.split())

# Remark
# There is also solution where we put all our dictionary to set. Let words have w1,…wk be lengths of
# words in split string, then we have time complexity O(∑i=1kw2k) and space complexity O(∑i=1kwk)=O(n).
# It sound like big number, but it is quite fast in python.
