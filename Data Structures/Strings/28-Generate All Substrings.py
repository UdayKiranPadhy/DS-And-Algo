"""
https://www.geeksforgeeks.org/print-all-the-combinations-of-a-string-in-lexicographical-order/

generate all possible strings of a Given String
Input: str = "ABC"
Output:
A
AB
ABC
AC
ACB
B
BA
BAC
BC
BCA
C
CA
CAB
CB
CBA

"""

# Approach 1
# generate all subsets, then generate their permutations

"""

#include "bits/stdc++.h"
using namespace std;

int main() {
    string s = "ABC";
    int n = s.size();
    vector <string> v;
    for(int mask = 0; mask < (1 << n); mask++) {
        string a;
        for(int i = 0; i < n; i++)
            if(mask & (1 << i)) a += s[i];

        do {
            v.push_back(a);
        } while(next_permutation(a.begin(), a.end()));
    }

    sort(v.begin(), v.end());
    for(string &a: v) cout << a << "\n";
}

"""


def get_permutations(s: str) -> list[str]:
    permutations = [[]]
    for char in s:
        permutations += [
            prev[:i] + [char] + prev[i:]
            for prev in permutations
            for i in range(len(prev) + 1)
        ]
    return ["".join(perm) for perm in permutations]


def get_permutations(s: str) -> list[str]:
    permutations = [[]]
    for char in s:
        new_permutations = []
        for prev in permutations:
            for i in range(len(prev) + 1):
                new_permutations.append(prev[:i] + [char] + prev[i:])
        permutations += new_permutations
    return ["".join(perm) for perm in permutations]
