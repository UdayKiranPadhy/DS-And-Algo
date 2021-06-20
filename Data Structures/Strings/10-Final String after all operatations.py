"""
Source :- CodeHers Exam
Date :- 13/06/21

Problem Statement
An e-commerce site is planning to launch a game. In the game, you will be given a 
string initially and some Q queries, for each query you will have 2 integers L 
and R. For each query, you have to perform the following operations:

Arrange the letters from L to R inclusive to make a Palindrome. If you can form 
many such palindromes, then take the one that is lexicographically minimum. Ignore 
the query if no palindrome is possible on rearranging the letters.
You have to find the final string after all the queries.

Constraints:
- 1 <= Length(S) <= 10^5
-1 <= Q<= 10^5
-1<= L <= R <= Length(S)

Input Format

First-line consists of the length of string S,
Second-line contains the string S itself and the number Q separated by space.
The next Q lines consist of two integers L and R separated by space.

Output Format

Print the string formed after all the operations.

Sample Testcase #0

Testcase Input
4
mmcs 1
1 3
Testcase Output
mcms

Explanation:-
The initial string is mmcs, there is 1 query which asks to make a 
palindrome from 1 3, so the palindrome will be mcm. Therefore the string will mcms.
"""

from collections import OrderedDict


def can_be_palindrom(string):
    """
    Function which checks weather a string can be a palindrom or not
    """

    # Sort the letters of string so that we can return lexicological minimum palindrome
    gg = sorted(string.lower(), key=lambda x: ord(x))
    # Can't store in normal dict , this Dictionary preserves the order of insertation
    alpha = OrderedDict()

    # Traverse through the list of all character and count the frequency
    for i in gg:
        if i in alpha:
            alpha[i] += 1
        else:
            alpha[i] = 1

    # Now see the frequency we can decide weather the string can be a palindrom or not
    N = len(gg)
    if N % 2 == 0:
        # All frequency count should be even
        palin = True
        for i in alpha:
            if alpha[i] % 2 != 0:
                palin = False
                break
    else:
        # There must be only character with odd count and rest must be even count to satisy palindrome
        palin = True
        odd = True  # Allow one character to be odd
        for i in alpha:
            if alpha[i] % 2 != 0:
                if odd:
                    odd = False
                else:
                    palin = False
                    break
    return palin, alpha


def make_palindrom(string, alpha):
    """
    Make lexicologically smallest palindrom using the alpha.

    Procedure:
    We need to place the char having odd count in the middle of the string.
    And even count character starting from starting index and ending index.
    """
    N = len(string)
    l = [0]*N
    i = 0
    j = N-1
    for char in alpha:

        if alpha[char] % 2 != 0:
            # if the character have odd frequency place it in middle
            l[N//2] = char
            alpha[char] -= 1
        else:
            # if the character have even frequency place it at stating and ending positions at same time
            while alpha[char] != 0:
                l[i] = char
                l[j] = char
                i += 1
                j -= 1
                alpha[char] -= 2

    # return the list in the form of string
    return "".join(l)


def main():
    # code Starts from here
    _ = int(input())
    string, q = input().split(" ")
    queries = []
    for i in range(int(q)):
        queries.append([int(x) for x in input().split(" ")])

    # For each queries
    for l, r in queries:
        # yes_or_no is variable True or False weather a string can be palin or not
        # Alphabets are dictionary contating frequency of character
        yes_or_no, alphabets = can_be_palindrom(string[l-1:r])
        if yes_or_no:
            # If string can be palindrome change the string
            string = string[:l-1] + \
                make_palindrom(string[l-1: r], alphabets)+string[r:]
        else:
            # Continue
            continue
    print(string)


if __name__ == '__main__':
    main()
