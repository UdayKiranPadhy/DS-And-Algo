"""

17. Letter Combinations of a Phone Number
Medium

7147

565

Add to List

Share
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""

# Solution 1  Itertools . product
# One way to solve this problem is to do backtracking.
# However we can use functionality of python product function, which
# will do almost everything for us. What is product? It is casterian
# product of two objects, for example if we have ob1 = [a, b, c] and ob2 = [d, e],
# then product(ob1, ob2) = [ad, bd, cd, ae, be, ce]. And this is almost what we need:

# In fact what will be returned are lists, so we need to join them.
# We need product of not 2 but several objects, and we will use * notation for this.
# Complexity
# Both time and space is O(3^m*4^n*(m+n)), where m is number of digits for which we
# have 3 options and n is number of letters for which we have 4 options, because
# we have 3^m*4^n options with m+n length each.


from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        return ["".join(gg) for gg in product(*[d[i] for i in digits])]



# Solution 2 My Trail DFS

class Solution2:
    def letterCombinations(self, digits: str) -> list[str]:
        if digits == "":
            return []
        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def flatten(l):      
            out = []
            for item in l:
                if isinstance(item, (list, tuple)):
                    out.extend(flatten(item))
                else:
                    out.append(item)
            return out

        def dfs(length, prev):
            if length == len(digits):
                return prev
            ans = []
            gg = digits[length]
            for i in d[gg]:
                ans.append(dfs(length+1, prev + i))
            return ans
        pypy = dfs(0, "")
        return flatten(pypy)

model = Solution2()
print(model.letterCombinations("23"))
