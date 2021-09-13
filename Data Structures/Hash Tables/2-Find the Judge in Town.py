"""

997. Find the Town Judge
Easy

In a town, there are n people labeled from 1 to n. There is a rumor that one of 
these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person 
labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, 
or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: n = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

Example 6:

Input: n = 1, trust = []
Output: 1

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n

"""

# Perfect Example for Hash Tables and Sets
# Maintain a Hash Table which stores the frequency a person is trusted
# Maintain in Unordered Set which stores the people are possibly the judge

# As soon as a person trusts someone he is not eligible for the judge so remove from the set
# Increase the frequency of the number to which he trusts


class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # Corner Case
        if n == 1 and trust == []:
            return 1

        # Generate Set
        numbers = set([i for i in range(1, n+1)])
        # Dictionary to count the frequency
        trusts = {}

        for i in trust:
            if i[0] in numbers:
                numbers.remove(i[0])
            if i[1] in trusts:
                trusts[i[1]] += 1
            else:
                trusts[i[1]] = 1

        for i in trusts.keys():
            if trusts[i] == n-1 and i in numbers:
                return i
        return -1
