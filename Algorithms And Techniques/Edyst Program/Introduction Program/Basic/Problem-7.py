# Reverse Parts Of String

"""
Write a program to take input a line from stdin. You have to reverse every word of this line, except for the starting and ending line of the words. For example, for the following input:

we love coding in this world
the output is:

we lveo cnidog in tihs wlrod
every word has been reversed except it's first and last alphabet.
Input format:

first line contains the number of lines, n
this is followed by n lines
Output:

print each line such that the words are reversed as per the criteria above
Example Input:
5
hello all
this is a good
example
to show you how to reverse
a string
 
Output:
hlleo all 
tihs is a good 
elpmaxe 
to sohw you how to rsrevee 
a snirtg

"""


def reverse(s):
    if len(s) <= 2:
        return s
    else:
        tr = s[1 : len(s) - 1]
        tr = tr[::-1]
        return s[0] + tr + s[len(s) - 1]


t = int(input())
l = []
for i in range(t):
    l.append(input())
for item in l:
    h = item.split(" ")
    r = ""
    for i in h:
        r += str(reverse(i)) + " "
    print(r)