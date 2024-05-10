"""

URL: https://leetcode.com/problems/evaluate-division/description/

399. Evaluate Division

UberAmazonGoogleFacebookSnapchatYou are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 
Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

 
Constraints:

	1 <= equations.length <= 20
	equations[i].length == 2
	1 <= Ai.length, Bi.length <= 5
	values.length == equations.length
	0.0 < values[i] <= 20.0
	1 <= queries.length <= 20
	queries[i].length == 2
	1 <= Cj.length, Dj.length <= 5
	Ai, Bi, Cj, Dj consist of lower case English letters and digits.

"""
from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)

        # Step 1). build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        def getTotal(source, dest, current=1):
            seen.add(source)
            result = -1
            neibours = graph[source]
            if dest in neibours:
                result = current * neibours[dest]
            else:
                for next, value in neibours.items():
                    if next not in seen:
                        result = getTotal(next, dest, current * value)
                        if result != -1:
                            break
            seen.remove(source)
            return result

        result = []
        for source, dest in queries:
            if source not in graph or dest not in graph:
                result.append(-1)
            elif source == dest:
                result.append(1)
            else:
                seen = set()
                result.append(getTotal(source, dest))
        return result