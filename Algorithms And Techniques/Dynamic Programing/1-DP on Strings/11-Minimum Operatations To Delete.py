"""
Source:- CodeHers Exam
Date :- 14-6-21

C P8
Problem Statement
Tokyo finds that her boyfriend Rhio is cheating on him and she is in a fit of rage. 
She wants to destroy Rhio before exiting his life. Rhio has some crucial information 
stored with him in the form of strings. Tokyo knows that if Rhio loses the data, 
it would be a substantial loss for him so she decides to delete the data.
Now, it takes m operations to delete an m digit number. She does not have this 
much of time so, she asks her guardian angel, the Professor to think of a way out.


He devises a method which says that she can delete parts of the number that have 
same digits consecutively i.e in one go. She could even concatenate the adjacent 
strings and delete them as a complete number if the above condition is satisfied.
Now, she wants to know the minimum number of operations needed to delete all 
the data using the method. You need to help her to do so.

Given n positive integers, find the minimum number of operations required to 
delete all of them

• 1<=T≤100
• 1<=n≤30
1 ≤ Si < 10^10

Input Format

First-line will input T, number of test cases.
The next pair of lines will input n and the respective numbers S₁,S2...Sn in the next line.

Output Format

For every test case, output the required minimum number of operations to delete all of the numbers.

Sample Testcase #0
Testcase Input
2
3
111 1111 111 
4
123 456 677 77

Testcase Output
1
7

Explanation
111, 1111 and 111 can be concatenated and deleted taking 1 operation, as 
all 1 can be deleted together.
123 can be deleted separately taking 3 operations.
456, 677 and 77 can be concatenated together and can be deleted in 4 operations, 
as in 45667777 "66" can be deleted together and "7777" can be deleted together. 
Therefore total operations are 7.

Sample Testcase #1
Testcase Input
2 
4 
90071 5111 23443 22 
3
789 987 789
Testcase Output
8 5

Explanatation:-
Conside 789 987 789
1st we cancel "99" and so the string becomes 7887789
next cut "88" and then the string becomes 77789
so remaing 3 cuts.
"""

import sys
from functools import lru_cache


def continous(string, i):
    if string[i] == string[i+1]:
        return True
    return False


def last_range(string, i):
    j = i
    while j <= len(string)-1 and string[j] == string[i]:
        j += 1
    return j


@lru_cache(None)
def mincount(string):
    if string == "":
        return 0
    if len(string) == 1:
        return 1
    else:
        mini = sys.maxsize
        for i in range(len(string)-1):
            if continous(string, i):
                j = last_range(string, i)
                mini = min(mini, 1 + mincount(string[:i]+string[j:]))
            else:
                mini = min(mini, 1 + mincount(string[:i]+string[i+1:]))
    return mini


for case in range(int(input())):
    _ = int(input())
    string = input().strip().replace(" ", "")
    print(mincount(string))