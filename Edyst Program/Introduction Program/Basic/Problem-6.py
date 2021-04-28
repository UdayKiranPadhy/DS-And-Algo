# Hollow Diamond Pattern Using Stars

"""
Write a program to take number n and print a Hollow Diamond shape .

Input Format:

Take an Integer from stdin.

Output:

Print the desired Pattern

Example Input:
5

Output:

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    * 

"""
n = int(input())
space = n - 1
for i in range(n):
    for s in range(space):
        print(" ", end="")
    space -= 1
    print("*", end="")
    for j in range(2 * (i - 1) + 1):
        inner_space = 2 * (i - 1) + 1
        print(" ", end="")
    if i != 0:
        print("*")
    else:
        print()
space += 2
inner_space -= 2
while n - 1:
    for s in range(space):
        print(" ", end="")
    space += 1
    print("*", end="")
    for i in range(inner_space):
        print(" ", end="")
    if n - 2 == 0:
        print()
    else:
        print("*")
    inner_space -= 2
    n -= 1

# while n:
#     for i in range(space):
#         print(" ", end="")
#     space -= 1
#     print("*")
#     for i in range(inner_space):
#         print(" ", end="")
#     inner_space += 1
#     if n != 0:
#         print("*")
#     print()
#     n -= 1