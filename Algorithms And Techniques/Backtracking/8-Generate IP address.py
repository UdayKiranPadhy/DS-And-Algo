"""
Date :- 29/06/21
Soucre :- Geeks For Geeks

Generate IP Addresses 

Given a string S containing only digits, Your task is to complete the function genIp() 
which returns a vector containing all possible combination of valid IPv4 ip address and 
takes only a string S as its only argument.
Note : Order doesn't matter.

For string 11211 the ip address possible are 
1.1.2.11
1.1.21.1
1.12.1.1
11.2.1.1

Example 1:

Input:
S = 1111
Output: 1.1.1.1

Your Task:

Your task is to complete the function genIp() which returns a vector containing all possible combination of valid IPv4 
ip address in sorted order and takes only a string S as its only argument.

Expected Time Complexity: O(N * N * N * N)
Expected Auxiliary Space: O(N * N * N * N)

Constraints:
1<=N<=16
here, N = length of S.
S only contains digits(i.e. 0-9)

Company Tags
 Amazon
Topic Tags
 Backtracking Strings


"""
ips = []


def GenerateIPAdress(s: str):
    def CanPlace(s, index, last_dot):
        gg = s[last_dot+1:index]
        try:
            gg = int(gg)
            if gg >= 0 and gg <= 255:
                return True
            else:
                return False
        except:
            return False

    def Place(string, i):
        return string[:i]+'.'+string[i:]

    def Remove(string, i):
        return string[:i] + string[i+1:]

    def backtrack(index, dot, string, last_dot):
        if dot == 0 and index <= len(string):
            ips.append(string)
            return
        for i in range(index, len(string)):
            if CanPlace(string, i, last_dot):
                string = Place(string, i)
                backtrack(i+1, dot-1, string, i+1)
                string = Remove(string, i)
        return

    backtrack(0, 4, s, -1)


s = '11211'
GenerateIPAdress(s)
