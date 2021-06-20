"""

You are given a list of strings each having 2 components to it - word and integer. These 2 components are separated by :.

If the square of digits in the number component is even, then you must rotate the word to the right by 1
If the square of digits in the number component is odd, then you must rotate the word to the left by 2
Finally, print the rotated word.

Example Input

rhdt:246,ghftd:1246
Output

trhd
ftdgh
Explanation

2*2+4*4+6*6 = 56 which is even so rotate rhdt --> trhd

1*1+2*2+4*4+6*6 = 57 which is odd so rotate ghftd --> ftdgh
"""
def isEven(k):
    sum=0
    for i in k:
        sum = sum + (int(i)**2)
    if sum%2==0:
        return True
    return False

k=input()
for i in k.split(","):
    string,k = i.split(":")
    if isEven(k):
        print(string[len(string)-1]+string[:-1])
    else:
        print(string[2:]+string[:2])