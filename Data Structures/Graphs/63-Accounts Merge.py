"""

URL: https://leetcode.com/problems/accounts-merge/description/

721. Accounts Merge

FacebookAppleGoogleTwitterAmazonGiven a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 
Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

 
Constraints:

	1 <= accounts.length <= 1000
	2 <= accounts[i].length <= 10
	1 <= accounts[i][j].length <= 30
	accounts[i][0] consists of English letters.
	accounts[i][j] (for j > 0) is a valid email.

"""
from collections import defaultdict
from typing import List


# [
# ["John","johnsmith@mail.com","john_newyork@mail.com"],
# ["John","johnsmith@mail.com","john00@mail.com"],
# ["Mary","mary@mail.com"],
# ["John","johnnybravo@mail.com"]
# ]

class DisjointSetUnion:
    def __init__(self, N: int):
        self.parent = list(range(N))
        self.size = [1] * N
        self.comp = N

    def find(self, a: int) -> int:
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a:
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a

    def union(self, u: int, v: int) -> None:
        a, b = self.find(u), self.find(v)
        if a == b:
            return
        if b > a:
            a, b = b, a
        self.size[a] += self.size[b]
        self.parent[b] = a
        self.comp -= 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        dsu = DisjointSetUnion(N)
        mappings = {}

        for idx, account in enumerate(accounts):
            name = account[0]
            for i in range(1, len(account)):
                email = account[i]
                if email in mappings:
                    parent = mappings[email]
                    dsu.union(parent, idx)
                mappings[email] = idx

        for key, value in mappings.items():
            mappings[key] = dsu.find(value)

        result = defaultdict(list)
        for key, value in mappings.items():
            result[value].append(key)

        final = []
        for key, value in result.items():
            name = accounts[key][0]
            merged = [name]
            merged.extend(sorted(value))
            final.append(merged)
        return final
