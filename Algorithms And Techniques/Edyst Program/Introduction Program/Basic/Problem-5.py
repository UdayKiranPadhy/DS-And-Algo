# Inverted Full Pyramid

"""

Given an integer n as input, print an inverted full pyramid of n rows.

Input Format:

Take input an integer from stdin
Output Format:

Print the pattern
Example Input:
10

Output:

* * * * * * * * * * 
 * * * * * * * * * 
  * * * * * * * * 
   * * * * * * * 
    * * * * * * 
     * * * * * 
      * * * * 
       * * * 
        * * 
         * 


"""

n = int(input())
step = 0
m = n

while n:
    for i in range(step):
        print(" ", end="")
    for i in range(m):
        print("* ", end="")
    print()
    m -= 1
    n -= 1
    step += 1
