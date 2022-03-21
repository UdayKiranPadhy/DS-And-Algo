"""
Date :- 21/06/21
Source :- Edyst

Prime Ring
A ring is composed of n (even number) circles as shown in diagram. 
Put natural numbers 1, 2, . . . , n into each circle separately, and 
the sum of numbers in two adjacent circles should be a prime.

Note: the number of first circle should always be 1.

Input
n (0 < n ≤ 16)

Output
The output format is shown as sample below. Each row represents a series 
of circle numbers in the ring beginning from 1 clockwisely and 
anticlockwisely. The order of numbers must satisfy the above requirements.

You are to write a program that completes above process.

Sample Input
6
Sample Output
1 4 3 2 5 6
1 6 5 2 3 4
Sample Input
8
Sample Output
1 2 3 8 5 6 7 4
1 2 5 8 3 4 7 6
1 4 7 6 5 8 3 2
1 6 7 4 3 8 5 2

"""

n = int(input())
