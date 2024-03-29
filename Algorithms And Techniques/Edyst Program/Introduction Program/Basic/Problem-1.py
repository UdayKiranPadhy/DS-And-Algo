# Print Fibonici Numbers

"""
In Fibonacci series, the next number is the sum of previous two numbers. 
The series starts with 0 and 1, and then the next numbers are a sum of the previous 2 numbers.

For example 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 etc.

Here the first 2 numbers are 0 and 1

The next numbers are:

1 (= 1 + 0)
2 (= 1 + 1)
3 (= 2 + 1)
5 (= 3 + 2)
And so on…

Write a program the first n numbers of the Fibonacci series.

Hint: You already know the first 2 values. How can you calculate the remaining?

Input Format
The first line contains T the number of test cases.

The following T lines contain n, the input for the Fibonacci Series.

Output Format
Print the values on a single line, separated by a space character. 
At the end of the line, print a new line.

Sample Input / Output
Input

5
3
4
8
9
7

Output
0 1 1
0 1 1 2
0 1 1 2 3 5 8 13
0 1 1 2 3 5 8 13 21
0 1 1 2 3 5 8

"""


t = int(input())
list1 = []
while t:
    list1.append(int(input()))
    t -= 1
for n in list1:
    f1 = 0
    f2 = 1
    if n == 1:
        print(f1)
        continue
    if n == 2:
        print(f1, end=" ")
        print(f2)
        continue
    print(f1, end=" ")
    print(f2, end=" ")
    n = n - 2
    while n:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        print(f3, end=" ")
        n -= 1
    print()