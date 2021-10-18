"""

745. Prefix and Suffix Search
Hard

856

303

Add to List

Share
Design a special dictionary with some words that searchs the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary, which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
 

Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
 

Constraints:

1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.

"""

# https://www.youtube.com/watch?v=U7fIQ7qAeuE&ab_channel=AlgorithmsMadeEasy

from collections import defaultdict
from typing import DefaultDict, List


class Trie_Node():
    def __init__(self) -> None:
        self.children = defaultdict()
        self.indexes = set()


class Trie:
    def __init__(self) -> None:
        self.root = Trie_Node()

    def insert(self, word, index):
        curr = self.root
        for letter in word:
            curr = curr.children.setdefault(letter, Trie_Node())
            curr.indexes.add(index)
        curr = curr.children.setdefault("_end")

    def search(self, word):
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return -1
            curr = curr.children[letter]
        return curr.indexes


class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = Trie()
        self.suffix = Trie()
        for index, word in enumerate(words):
            self.prefix.insert(word, index)
            self.suffix.insert(word[::-1], index)

    def f(self, pref: str, suff: str) -> int:
        pre = self.prefix.search(pref)
        suf = self.suffix.search(suff[::-1])
        if pre == -1 or suf == -1:
            return -1
        common = pre.intersection(suf)
        if len(common) == 0:
            return -1
        else:
            return max(list(common))
