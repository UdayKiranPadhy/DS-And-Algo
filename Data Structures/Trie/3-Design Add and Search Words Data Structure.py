"""

https://leetcode.com/problems/design-add-and-search-words-data-structure/description/

211. Design Add and Search Words Data Structure
Medium

3535

148

Add to List

Share
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.

"""

from collections import defaultdict
from typing import DefaultDict


# https://leetcode.com/problems/design-add-and-search-words-data-structure

# In this problem, we need to use Trie data structure. For more details
# go to the problem 208. Implement Trie (Prefix Tree).

# So, what we have here?

# TrieNode class with two values: dictionary of children and flag, if this
# node is end of some word.
# Now, we need to implement addWord(self, word) function: we add symbol
# by symbol, and go deepere and deeper in our Trie. In the end we note
# our node as end node.
# Now, about search(self, word) function. Here we use dfs(node, i) with
# backtracking, because we can have symbol . in our word (here node is
# link to Trie node and i is index of letter in word). So we need to check
# all options: we go to all possible children and call dfs recursively.
# If we found not ., but just some letter, we check if we have this letter
# as children, and if we have, we go deeper. If we are out of letters,
# that is i == len(word), we return True if current end_node is equal to
# 1 and false in opposite case. Finally, we return False if we can not go
# deeper, but we still have letters.
# Now, we just return dfs(self.root, 0).
# Complexity: Easy part is space complexity, it is O(M), where M is sum
# of lengths of all words in our Trie. This is upper bound: in practice
# it will be less than M and it depends, how much words are intersected.
# The worst time complexity is also O(M), potentially we can visit all our
# Trie, if we have pattern like ...... For words without ., time complexity
# will be O(h), where h is height of Trie. For words with several letters
# and several ., we have something in the middle.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = 0


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        root = self.root
        for symbol in word:
            root = root.children.setdefault(symbol, TrieNode())
        root.end_node = 1

    def search(self, word):
        def dfs(node, i):
            if i == len(word):
                return node.end_node

            if word[i] == ".":
                for child in node.children:
                    if dfs(node.children[child], i+1):
                        return True

            if word[i] in node.children:
                return dfs(node.children[word[i]], i+1)

            return False

        return dfs(self.root, 0)
