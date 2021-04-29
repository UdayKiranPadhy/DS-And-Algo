"""
Longest Palindromic Subsequence
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some 
or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".


Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
"""

# Solution
"""
2. If you are given only one string

/* Pre-processing. Define basic cases. */
for( int len = 1; len < n; len++){
	for( int i = 0; i + len < n; i++){
		int j = i + len;
		if(s1[i - 1] == s1[j - 1]){
			/* Your code */
		}
		else{
			/* Your code */
		}
	}
}
"""

"""
STEP 1: Understand the question.
Return length of the longest palindrome subsequence.

STEP 2: Base Cases
Every single character is a palindrome.
What does a cell in the table or vector means? Maximum length of palindrome that exists between i and j.

STEP 3: Main definition.
It varies since single string is given. The code looks like interval dp problems.

What if two characters are matching? we have return 2 + dp[i + 1][j - 1].
Why? 2 for the two characters & then find for the interval i + 1 and j - 1.
What if two characters are not matching? We have find maximum between 
two subproblems (dp[i + 1][j] and dp[i][j - 1] )

1) Optimal Substructure: 
Let X[0..n-1] be the input sequence of length n and L(0, n-1) be the length of the longest palindromic subsequence of X[0..n-1]. 
If last and first characters of X are same, then L(0, n-1) = L(1, n-2) + 2. 
Else L(0, n-1) = MAX (L(1, n-1), L(0, n-2)).
"""


def LPS(string: str, m: int, n: int) -> int:
    # Base Case
    # If there is only one character
    if m == n:
        return 1

    if m > n:
        return 0
    # If last and the first Characters are same then
    if string[m] == string[n]:
        return 2 + LPS(string, m + 1, n - 1)

    # if character of n and the character of m are not equal
    else:
        return max(LPS(string, m + 1, n), LPS(string, m, n - 1))


# word = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
# print(LPS(word, 0, len(word) - 1))

# print(len(word)) #472

# As we saw the time and complexity for that word so we go with memorization


def LPS2(string):
    m = len(string)
    dp = [[0] * m for _ in range(m)]

    for i in range(m):
        dp[i][i] = 1

    # Template for our question
    # for( int len = 1; len < n; len++){
    # 	for( int i = 0; i + len < n; i++){
    # 		int j = i + len;
    # 		if(s1[i - 1] == s1[j - 1]){
    # 			/* Your code */
    # 		}
    # 		else{
    # 			/* Your code */
    # 		}
    # 	}
    # }
    for length in range(1, m):
        i = 0
        while i + length < m:
            j = i + length
            if string[i] == string[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
            i += 1
    return dp[0][-1]


print(
    LPS2(
        "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
    )
)
# Now see the Speed (GG Speed)
# https://leetcode.com/problems/longest-palindromic-subsequence/

# Method 2 using template 1


def LPS3(s):
    t = reversed(s)
    # t= s[::-1]
    dp = [[0 for _ in range(len(t) + 1)] for __ in range(len(s) + 1)]
    for i in range(1, 1 + len(s)):
        for j in range(1, 1 + len(t)):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]
