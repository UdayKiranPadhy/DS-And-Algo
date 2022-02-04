"""

797. All Paths From Source to Target
Medium

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from 
node i (i.e., there is a directed edge from node i to node graph[i][j]).

 

Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
Example 3:

Input: graph = [[1],[]]
Output: [[0,1]]
Example 4:

Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]
Example 5:

Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]
 

Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.

"""

# We are given a DAG consisting of n nodes from 0 to n-1 and we need to return all paths from 0 to n-1.

# ✔️ Solution - I (BFS)

# We can start from the starting node 0 and traverse every possible next node from the current node.
# Whenever we reach the last node n-1, we will add the path till now into the final answer.
# This process can be implemented using a BFS traversal as -

# 1-Initialize a queue of path of nodes with the node 0 inserted into it initially denoting the starting
# node in our traversal path from 0 to n-1
# 2-Pop an element path from the queue
# 3-Explore every child node of last node in the path. That is, we try every possible edge in graph
# from node at the end of current path. Each edge added to end of path gives us another path which will be added to queue for further exploration
# 4-If the last node in path is n-1, we know that this is a valid source to target path in the graph. So, we add it to final list of paths
# We repeat this process until the queue is not empty, that is, until there are paths remaining to be explored.
# C++

# class Solution {
# public:
#     vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& G) {
#         vector<vector<int>> ans;
#         queue<vector<int>> q;
#         q.push({0});                                                   // starting node of every path
#         while(size(q)) {
#             auto path = move(q.front()); q.pop();
#             if(path.back() == size(G)-1) ans.push_back(move(path));    // found valid path
#             else
#                 for(auto child : G[path.back()]) {                     // try every possible next node in path
#                     path.push_back(child);
#                     q.push(path);                                      // push path into queue for further exploration
#                     path.pop_back();
#                 }
#         }
#         return ans;
#     }
# };

# Python

from typing import Deque, List


class Solution:
    def allPathsSourceTarget(self, G):
        ans, q = [], Deque([[0]])
        while q:
            path = q.pop()
            if path[-1] == len(G) - 1:
                ans.append(path)
            else:
                for child in G[path[-1]]:
                    q.append(path + [child])
        return ans


# Time Complexity : O(2N), where N is the number of nodes in the graph. Every node except the start and end node of graph can either be part of a path or not be part of a path. For a path consisting of k (3 <= k <= n) nodes, we have k-2 intermediate nodes and we can choose from n-2 available nodes. Thus the resulting time complexity is Σ n-2Ck-2 for all 3 <= k <= n, which comes out to be O(2N-2) = O(2N)
# Space Complexity : O(2N)

# ✔️ Solution - II (DFS)

# We can also solve this problem using DFS traversal. This traversal should also be more efficient in terms of space usage as compared to BFS traversal since we are only required to keep a single path in memory at a given time. Note that we dont need to maintain a data structure such as seen to keep track of visited nodes since this is a DAG and thus no recursive dfs call will end up visiting same node twice.

# The process of finding all paths using DFS can be implemented as -

# Begin DFS traversal from the node 0
# At each step of DFS, add the current node i to the path.
# If the current node i in dfs call is n-1, we know that this is a valid source to target path in the graph. So, we add it to final list of paths.
# Otherwise, we explore further path by trying each possible next nodes, that is, we recursively call DFS for every child node of i in the graph.
# The above process continues till every possible path is tried out by dfs.
# C++

# class Solution {
# public:
#     vector<vector<int>> ans;
#     vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& G) {
#         vector<int> path;
#         dfs(G, 0, path);
#         return ans;
#     }
#     void dfs(vector<vector<int>>& G, int i, vector<int>& path) {
#         path.push_back(i);                            // add current node to path
#         if(i == size(G)-1) ans.push_back(path);       // valid path found
#         else
#             for(auto child : G[i])
#                 dfs(G, child, path);                  // recurse for every possible next node in path
#         path.pop_back();                              // backtrack
#     }
# };
# Alternate Implementation
# Python


class Solution:
    def allPathsSourceTarget(self, G):
        ans = []

        def dfs(path):
            if path[-1] == len(G) - 1:
                ans.append(path)
            else:
                for child in G[path[-1]]:
                    dfs(path + [child])

        dfs([0])
        return ans


# Time Complexity : O(2N), same as above
# Space Complexity : O(N), required by max recursive stack depth and for storing path.
# Generally output space is not considered towards overall space complexity.


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        ans = []

        def dfs(x, path):
            if x == N - 1:
                ans.append(path[:])
                return
            for n in graph[x]:
                path.append(n)
                dfs(n, path)
                path.pop()

        dfs(0, [0])
        return ans
