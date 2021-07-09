"""
Date :- 4/7/21
Source :- Leetcode

Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3: 

Input: n = 5
Output: 68
 

Constraints:

1 <= n <= 2 * 10^4

"""


# Solution - 1
# Brute Force or DFS

# We need to form a string of length n with vowels. We are also given
# some initial rules or mappings which tells us what character will come
# after the current character. We need to return the total number of
# different strings we can form.

# Let's try to solve this problem starting with the brute-force appraoch.
# We can start with any of the 5 vowels and thereafter we have the choice
# to choose next vowel depending on what's allowed after the previous vowel
# in the given mappings. The given mappings state what vowels are allowed
# after a given vowel -

# start   =>  a / e / i / o / u   # start denotes 1st character of string which can be any vowel
# a       =>  e
# e       =>  a / i
# i       =>  a / e / o / u
# o       =>  i / u
# u       =>  a
# So, we will follow this approach. At each index, we will try choosing all vowels
# allowed after the previous one. The start will be denoted by
# s (any vowel is allowed after it).

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        G = {
            "s": ["a", "e", "i", "o", "u"],
            "a": ["e"],
            "e": ["a", "i"],
            "i": ["a", "e", "o", "u"],
            "o": ["i", "u"],
            "u": ["a"]
        }
        MOD = pow(10, 9)+7

        def go(prev, rem):
            if rem == 0:
                return 1
            count = 0
            for neibour in G[prev]:
                count += go(neibour, rem-1) % MOD
            return count % MOD
        return go("s", n)

# Time Complexity : O(5^n), at each index we have maximum of 5 choices with us. There are total of n indices. Thus 5*5*5...n times = O(5n).
# Space Complexity : O(n), required for recursive stack. Max recursive depth at any point will be n


# Solution-2 (Dynamic Programming Top-Down Recursive Approach)
# We can observe does a lot of repeated calculations. The total number of possible strings
# when we know the previous character prev and remaining length rem will always be constant.
# So there's no need to repeat the same calculation. We can store the calculated result
# for a given state and reuse it in the future. Thus, we can optimize the solution using
# dynamic programming.

# We will maintain a dp array of length n+1 for each vowel. Here, dp[prev_vowel][rem] will
# denote the number of strings that can be formed when previous character was prev_vowel and
# number of characters still required is equal to rem. Each time, we will try all vowels
# possible at current index and explore the further path. We will store the calculated result
# in dp[prev][rem] and reuse it whenever required in future recursive calls.

"""
class Solution {
    const int MOD = 1e9 + 7;
    const unordered_map<char, vector<char>> mappings{ {'s', {'a', 'e', 'i', 'o', 'u'} }, // start
                                                      {'a', {'e'}                     }, 
                                                      {'e', {'a', 'i'}                }, 
                                                      {'i', {'a', 'e', 'o', 'u'}      }, 
                                                      {'o', {'i', 'u'}                },
                                                      {'u', {'a'}                     }  };
    unordered_map<char, vector<int>> dp;
public:
    int countVowelPermutation(int n) {
        dp['s'] = dp['a'] = dp['e'] = dp['i'] = dp['o'] = dp['u'] = vector<int>(n+1);
        return solve(n, 's');                         // start with s
    }
    int solve(int rem, char prev) {
        if(rem == 0) return 1;                        // no need to pick further. We have formed 1 string of length = n.
        if(dp[prev][rem]) return dp[prev][rem];       // if result already calculated for current state, directly return it
        for(auto c : mappings.at(prev))               // try each vowel allowed after prev character
            dp[prev][rem] = (dp[prev][rem] + solve(rem - 1, c)) % MOD;  
        return dp[prev][rem];
    }
};

Time Complexity : O(N), we will be calculating the total possible strings for a given vowels when rem characters are requried, only once. Thus, each vowel will make a max of N recursive calls. Hence the total time complexity becomes O(5*N) = O(N)
Space Complexity : O(N), O(N) space is required by recursive stack. Further, a total of O(5*N) space is used by dp. Thus the total space complexity becomes O(N) + O(5*N) = O(N)


"""
