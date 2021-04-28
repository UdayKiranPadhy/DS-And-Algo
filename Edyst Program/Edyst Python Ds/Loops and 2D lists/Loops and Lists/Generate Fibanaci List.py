"""
Estimated End Date: 18/02/21
Generate Fibonacci list
Complete the given method solve which accepts an integer n. You have to generate a list containing the first n+1 Fibonacci numbers.

Recap: Fibonacci numbers are those that are formed by summing up the previous 2 numbers in the series. The series starts with 0 and 1, and is then followed by : 1 2 3 5 8 13...
Return the generated list

Example Input:
1

Output:
0 1

Example Input:
6

Output:
0 1 1 2 3 5 8
"""
import math


def fib(x):
    # we used formula for finding nth term of fibonacci series.
    # Formula Fn={[(√5+1)/2]∧n}/√5.
    # Above formula you wil get after solving Fn=Fn-1+Fn-2 on given initial condition F[0]=0,F[1]=1.
    n = (math.sqrt(5) + 1) / 2
    # round function used to round the value Ex:- round(3.2)=3 ,round(3.6)=4
    return round(math.pow(n, x) / math.sqrt(5))


def solve(n):
    l = [0]
    for i in range(n):
        l.append(fib(i + 1))
    return l