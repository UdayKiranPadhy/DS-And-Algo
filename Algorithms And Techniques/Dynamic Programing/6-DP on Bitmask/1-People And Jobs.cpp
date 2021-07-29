/*

Problem Statement

Let there be N workers and N jobs. Any worker can be assigned to perform any job, 
incurring some cost that may vary depending on the work-job assignment. 
It is required to perform all jobs by assigning exactly one worker to 
each job and exactly one job to each agent in such a way that the total 
cost of the assignment is minimized.

Input Format
Number of workers and job: N
Cost matrix C with dimension N*N where C(i,j) is the cost incurred on 
assigning ith Person to jth Job.

Sample Input
4

[

People 1    9 2 7 8
People 2    16 4 3 7
People 3    5 8 1 8
People 4    7 6 9 4
]

Sample Output
13

Constraints
N <= 20

*/



#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int cost[21][21];
int dp[21][(1 << 21)];

int solve(int i, int mask, int n)
{
    if (i == n + 1)
    {
        return 0;
    }
    else if (dp[i][mask] != -1)
    {
        return dp[i][mask];
    }
    else
    {
        int minimum = INT_MAX;
        for (size_t j = 0; j < n; j++)
        {
            if (mask & (1 << j))
            {
                minimum = min(minimum, cost[j][i] + solve(i + 1, mask ^ (1 << j), n));
            }
        }
        return dp[i][mask] = minimum;
    }
}
int main()
{
    int n;
    cout << "Enter the size of array" << endl;
    cin >> n;
    memset(dp, -1, sizeof(dp));
    int cost[n][n];
    for (size_t i = 0; i < n; i++)
    {
        for (size_t j = 0; j < n; j++)
        {
            cin >> cost[i][j];
        }
    }
    cout << solve(0, (1 << n) - 1, n) << '\n';
}