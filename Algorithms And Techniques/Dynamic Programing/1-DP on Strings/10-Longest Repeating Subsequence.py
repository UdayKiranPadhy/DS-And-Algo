"""
Longest Repeated Subsequence
Given a string, print the longest repeating subsequence such that the two subsequence don’t have 
same string character at same position, i.e., any i’th character in the two subsequences 
shouldn’t have the same index in the original string.

Examples: 

Input: str = "aabb"
Output: "ab"

Input: str = "aab"
Output: "a"

The two subsequence are 'a'(first) and 'a' 
(second). Note that 'b' cannot be considered 
as part of subsequence as it would be at same
index in both.

Example 2 :

Input: str = "AABEBCDD"
Output: ABD

"""


def LRS(string):
    m = len(string)
    dp = [[0 for _ in range(m + 1)] for j in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, m + 1):
            if string[i - 1] == string[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j - 1])

    return dp[-1][-1]


"""
// Pseudo code to find longest repeated
// subsequence using the dp[][] table filled
// above.

// Initialize result
string res = "";

// Traverse dp[][] from bottom right
i = n, j = n;
while (i > 0 && j > 0)
{
   // If this cell is same as diagonally
   // adjacent cell just above it, then 
   // same characters are present at 
   // str[i-1] and str[j-1]. Append any 
   // of them to result.
   if (dp[i][j] == dp[i-1][j-1] + 1)
   {
       res = res + str[i-1];
       i--;
       j--;
   }

   // Otherwise we move to the side
   // that that gave us maximum result
   else if (dp[i][j] == dp[i-1][j])
      i--;
   else
      j--;
 }

 // Since we traverse dp[][] from bottom,
 // we get result in reverse order.
 reverse(res.begin(), res.end());

return res;
"""
