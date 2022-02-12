"""

127. Word Ladder
Hard

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

"""

# https://leetcode.com/problems/word-ladder/

from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        graph = defaultdict(list)
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        for word in wordList:
            for i in range(len(word)):
                part1 , part2 = word[:i] , word[i+1:]
                for alpha in alphabets:
                    new_word = part1 + alpha + part2
                    if new_word in wordset and new_word != word:
                        graph[word].append(new_word)
        q = deque([beginWord])
        length = 0
        visited = set()
        while q:
            for i in range(len(q)):
                popedElement = q.popleft()
                if popedElement == endWord:
                    return length + 1
                visited.add(popedElement)
                for child in graph[popedElement]:
                    if child not in visited:
                        q.append(child)
            length +=1
        return 0
      
model = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(model.ladderLength(beginWord,endWord,wordList))