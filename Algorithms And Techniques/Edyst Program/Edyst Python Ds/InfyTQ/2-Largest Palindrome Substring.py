"""
Take as input a string. Find the longest possible substring from this string which is also a palindrome.

Example Input

dcodocir

Output

codoc
"""
def isPalindrome(str1):
    if str1 == str1[::-1]:
        return True
    return False

string= input()
palindromes=[]
for i in range(len(string)):
    for j in range(i,len(string)+1):
        if isPalindrome(string[i:j]) and len(string[i:j])>1:
            palindromes.append(string[i:j])
max_len=-1
print(palindromes)
for i in palindromes:
    if len(i)>max_len:
        max_str=i
        max_len=len(i)
print(max_str)