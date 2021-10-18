"""
Date :- 03/06/21
Source :- https://leetcode.com/problems/similar-string-groups/

839. Similar String Groups
Hard

Two strings X and Y are similar if we can swap two letters (in different positions) of X, 
so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), 
and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  
Notice that "tars" and "arts" are in the same group even though they are not similar.  
Formally, each group is such that a word is in the group if and only if it is similar 
to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

 

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1
 

Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.

"""


class Solution:
    def numSimilarGroups(self, strs: list[str]) -> int:
        G = {}
        for i in strs:
            G[i] = [i]
        n = len(strs[0])
        for i in range(len(strs)):
            for j in range(i+1, len(strs)):
                count = 0
                for k, l in zip(strs[i], strs[j]):
                    if k != l:
                        count += 1
                        if count > 2:
                            break
                if count == 2:
                    G[strs[i]].append(strs[j])
                    G[strs[j]].append(strs[i])

        visited = set()
        comp = 0
        for i in G.keys():
            if i not in visited:
                comp += 1
                visited.add(i)
                stack = [i]
                while stack:
                    cur = stack.pop()
                    for new in G[cur]:
                        if new not in visited:
                            visited.add(new)
                            stack.append(new)
        return comp
