"""
Write a Program to take Integer as an Input.And to print the full  inverted hollow  pyramid using stars according to given Input.

Input Format:

Take Integer input from stdin

Output Format:

Print the desired pattern

Example Input:
6

Output:

* * * * * *
 *       *
  *     *
   *   *
    * *
     *

* * * * * * *
 *         *
  *       *
   *     *
    *   *
     * *
      *
"""
num = int(input())

for i in range(1, num+1):
    for j in range(0, i):
        print(" ", end="")

    for j in range(1, (num*2 - (2*i - 1))+1):
      if (i==1 and j%2!=0) or (j == 1 or j ==(num*2 -(2*i-1))):
            print("*", end="")
      else:
            print(" ", end="")
    print()