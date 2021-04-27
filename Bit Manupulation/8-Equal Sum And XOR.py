"""
Equal Sum and XOR
Given a positive integer n, find count of positive integers i 
such that 0 <= i <= n and n+i = n^i 

Examples : 
Input  : n = 7
Output : 1
Explanation:
7^i = 7+i holds only for only for i = 0
7+0 = 7^0 = 7

Input: n = 12
Output: 4
12^i = 12+i hold only for i = 0, 1, 2, 3
for i=0, 12+0 = 12^0 = 12
for i=1, 12+1 = 12^1 = 13
for i=2, 12+2 = 12^2 = 14
for i=3, 12+3 = 12^3 = 15
"""

"""
we know (a + b) = (a ^ b) + (a & b)
l.e. if a & b==0, implies a+b==a^b,
( This is quite intuitive and also evident from the half adder implementation)

Hence, we must find out pairs such that n & i == 0, to find out the solution to
n + i == n ^ i

Now, our problem reduces to:
=> Finding count of all possible values of 0 <= i <= in such that n & i = 0.?
How to find count of such pairs?
For n & i to be zero, i must unset all set-bits of n.

In other words,
If the kth bit is set at a particular in n, kth bit in i must be 0 always, else
if it is unset then, kth bit of i can be 0 or 1

let x be the no. of unset bits in n then the answer is 2^x
"""