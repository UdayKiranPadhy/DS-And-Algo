"""

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


class MagicDictionary:

    def __init__(self):
        self.root = DefaultDict()

    def buildDict(self, dictionary: List[str]) -> None:
        for words in dictionary:
            curr = self.root
            for letter in words:
                curr = curr.setdefault(letter, defaultdict())
            curr.setdefault("_end")

    def search2(self, word):
        curr = self.root
        for letter in word:
            if letter in curr:
                curr = curr[letter]
                continue
            return False
        if "_end" in curr:
            return True
        return False

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            curr = self.root
            letter = searchWord[i]
            for ch in string.ascii_lowercase:
                if ch == letter:
                    continue
                if self.search2(searchWord[:i]+ch+searchWord[i+1:]):
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
