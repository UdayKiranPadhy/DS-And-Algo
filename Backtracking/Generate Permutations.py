"""
Permutation
To print all the permutations of a string.

Sample Input:
ABC
Sample Output:
ABC
ACB
BAC
BCA
CAB
CBA
"""

def permutate(s):
    if len(s) == 0:
        return ""
    if len(s) == 1:
        return s
    else:
        for i in range(len(s)):
            # return permutate(s[:i]) + str(s[i]) + permutate(s[i:])
            return str(s[i]) + permutate(s[:i]+s[i+1:])
# print(permutate("ABC"))

"""
Second Trial
"""
def permutate2(s, ans=""):
    if len(s) == 0:
        print(ans)
        return
    else:
        for i in range(len(s)):
            ch = ans + s[i]
            ros = s[:i]+s[i+1:]
            permutate2(ros, ch)
            
permutate2("ABC")


"""
Time Complexity: O(N*2^n)
Space Complexity: O(2^n)
"""