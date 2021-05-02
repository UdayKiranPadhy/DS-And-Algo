"""
Edit Distance
Hard
Given two strings word1 and word2, return the minimum number of operations 
required to convert word1 to word2.

You have the following three operations permitted on a word:
Insert a character 
Delete a character 
Replace a character 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 
Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""

# Solution
"""
Step 1: Read the problem and try to understand it (Hardest Part)
Let's take this problem and find out what it says!

Two strings will be provided to you (Ex. horse and ros).
You can make 3 operations (Insert, Delete, Replace).
We have to find the minimum no. of operations to convert string1 to string2.



Step 2: Pre Processing (Tabulation & Define Base Cases)

We have to tabulate the answers for subproblems in order to use it again.
What is a cell in table means? dp[i,j] has the answer for the subproblem string1(:i) and string2(:j)

Define Base Cases. It varies from problem to problem.
In this problem the base cases are,

What if the string1 and string2 are empty?
What if the string1 is empty and string2 is not empty and vice versa?
Lets find it out.

Both String1 and String2 are empty: Then the answer to the subproblem is 0. Since minimum operations to be 
performed to make string1 as string2 is 0.
String1 is empty and String2 is not empty: We need insert characters to make it as string2. 
Minimum operations to be performed will be equal to string2 length.
String1 is not empty and String2 is empty: We have delete characters to make it as string2.

Step 3:
The main problem definition goes here.

If both the string have same character we don't have do any operations, So that min no of operations to be performed is equal to subproblem with state (i - 1, j - 1).
If characters are different, we can do three operations (Insert, Delete, Replace) We can find minimum between subproblems with states( dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j] ) + 1.
Why these states?

dp[i - 1][j - 1] => If we replace the character.
dp[i][j - 1] => If we delete the character.
dp[i - 1][j] => If we insert the character.
Return dp[string1.length][string2.length]. Since it contains the answer for subproblem between two strings.
"""

# Naive Recursive Approach


def editDistance(string1, string2, m, n):
    # base cases

    # If first string is empty, the only option is to
    # insert all characters of second string into first
    if m == 0:
        return n

    # If the second string is empty, the only option is to
    # delete all the characters
    if n == 0:
        return m

    # If last two characters are same , nothing much can be done
    # Just check the remaing string characters
    if string1[m - 1] == string2[n - 1]:
        return editDistance(string1, string2, m - 1, n - 1)

    else:
        return 1 + min(
            editDistance(string1, string2, m - 1, n - 1),
            editDistance(string1, string2, m, n - 1),
            editDistance(string1, string2, m - 1, n),
        )


# print(editDistance("Uday", "Usha", 4, 4))

# The time complexity of above solution is exponential.
# In worst case, we may end up doing O(3^m) operations.
# The worst case happens when none of characters of two strings match.


# Method-2

# The invariant maintained throughout the algorithm is that we can transform the
# initial segment X[1.i] into Y[1..j] using a minimum of T[i, j] operations. In
# the end, the bottom-right array element contains the answer.

# For example, let X be 'kitten', and Y be sitting' The Levenshtein distance between
# X and Y is 3. The i'th row and j'th column in the table below show the
# Levenshtein distance of substring x[0...i-1] and Y[0..j-1] .
#        u  d  a  y
#    [0, 1, 2, 3, 4],
# a  [1, 1, 2, 3, 4],
# j  [2, 2, 2, 3, 4],
# a  [3, 3, 3, 2, 3],
# y  [4, 4, 4, 3, 2]


# Recursive Memorizatation Bottom-up


def editDistance2(string1, string2, m, n):
    global dp
    if dp[m][n]:
        return dp[m][n]
    else:
        if m == 0:
            dp[m][n] = n
            return n
        elif n == 0:
            dp[m][n] = m
        elif string1[m] == string2[n]:
            dp[m][n] = editDistance2(string1, string2, m - 1, n - 1)
            return dp[m][n]
        else:
            dp[m][n] = 1 + min(
                editDistance2(string1, string2, m - 1, n),
                editDistance2(string1, string2, m, n - 1),
                editDistance2(string1, string2, m - 1, n - 1),
            )
            return dp[m][n]


# print(editDistance("Uday", "Usha", 4, 4))

# Top - down Approach


def editDistance3(string1, string2):
    m = len(string1)
    n = len(string2)

    # For all pairs of `i` and `j`, `T[i, j]` will hold the Levenshtein distance
    # between the first `i` characters of `X` and the first `j` characters of `Y`.
    # Note that `T` holds `(m+1)×(n+1)` values.
    Cost = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            # if string 1 is empty then we have to append all the character of string 2
            if i == 0:
                Cost[i][j] = j
            # if string 2 is empty the we have to remove all the characters of string 1
            elif j == 0:
                Cost[i][j] = i

            # Now start check line wise bottom to top
            elif string1[i - 1] == string2[j - 1]:
                Cost[i][j] = Cost[i - 1][j - 1]

            else:
                Cost[i][j] = 1 + min(Cost[i - 1][j - 1], Cost[i][j - 1], Cost[i - 1][j])
    return Cost[-1][-1]


#        u  d  a  y
#    [0, 1, 2, 3, 4],
# a  [1, 1, 2, 3, 4],
# j  [2, 2, 2, 3, 4],
# a  [3, 3, 3, 2, 3],
# y  [4, 4, 4, 3, 2]
# print(editDistance2("Uday", "Ajay"))
