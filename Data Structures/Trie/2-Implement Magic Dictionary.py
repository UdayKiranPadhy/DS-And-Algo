"""
https://leetcode.com/problems/implement-magic-dictionary/
676. Implement Magic Dictionary
Medium

Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.

Implement the MagicDictionary class:

MagicDictionary() Initializes the object.
void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, otherwise returns false.
 

Example 1:

Input
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
Output
[null, null, false, true, false, false]

Explanation
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False
 

Constraints:

1 <= dictionary.length <= 100
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case English letters.
All the strings in dictionary are distinct.
1 <= searchWord.length <= 100
searchWord consists of only lower-case English letters.
buildDict will be called only once before search.
At most 100 calls will be made to search.

"""

from collections import defaultdict
import string
from typing import DefaultDict, List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0


class MagicDictionary:
    def __init__(self):
        self.roots = defaultdict(TrieNode)

    def buildDict(self, dictionary):
        for word in dictionary:
            root = self.roots[len(word)]
            for symbol in word:
                root = root.children.setdefault(symbol, TrieNode())
            root.end_node = 1

    def dfs(self, i, word, changes, pos):
        if changes == 0 and i == len(word) and pos.end_node == 1:
            return True

        for s in pos.children:
            if i < len(word) and (t := changes - (s != word[i])) >= 0:
                if self.dfs(i + 1, word, t, pos.children[s]): return True
        return False

    def search(self, searchWord):
        return self.dfs(0, searchWord, 1, self.roots[len(searchWord)])
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
