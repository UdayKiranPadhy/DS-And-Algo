"""
Printing Longest Common Subsequence
Difficulty Level : Medium

Given two sequences, print the longest subsequence present in both of them.
Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

# Looking care fully in the dp table of we need to trace it back words by comparing the top,
# side block of i,j and the top diagonal depending on the character of s[i] and s2[j]


def LCS(string1: str, string2: str) -> int:
    m = len(string1)
    n = len(string2)

    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    gg = ""
    for i in range(1, m + 1):
        gg2 = True
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if gg2:
                    gg += string1[j - 1]
                    gg2 = False
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    print(gg)
    return dp[-1][-1]


print(LCS("Uday", "Ajay"))


def lcs(X, Y, m, n):
    L = [[0 for x in xrange(n + 1)] for x in xrange(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Following code is used to print LCS
    index = L[m][n]

    # Create a character array to store the lcs string
    lcs = [""] * (index + 1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:

        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i - 1] == Y[j - 1]:
            lcs[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
