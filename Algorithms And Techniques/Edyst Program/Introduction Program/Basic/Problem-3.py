# Position Of Man

"""
A man from origin can move in below direction,
10 Mts right in first turn,
20 Mts up in second turn,
30 Mts left in third turn,
40 Mts down in fourth turn,
50 Mts right in fifth turn,

10 Mts right in sixth turn,
20 Mts up in seventh turn,
30 Mts left in eighth turn,
40 Mts down in ninth turn,
50 Mts right in tenth turn and so on


Write a program to print the position of man from origin in nth turn.
where 2<=n <= 1000.
n = no of turns.

Input Format:
Take integer from stdin.

Output Format:
print the position of man from origin.

Example Input:
3

Output:
-20 20

Explanation
In each turn the step size increases by 10. Also, the turns move from right, up, left, down and right then the same steps keeps repeating
In our case, man starts from (0,0) --> (10,0) --> (10,20) --> (-20,20)
Hence answer is (-20,20)
"""

current = [0, 0]
x = 1
y = 0
w = int(input())
for n in range(1, w + 1):
    m = n % 5
    if (m == 1) or (m == 0):
        x = 1
        y = 0
    if m == 2:
        x = 0
        y = 1
    if m == 3:
        y = 0
        x = -1
    if m == 4:
        x = 0
        y = -1
    if m == 0:
        m = 50
    else:
        m = m * 10
    current[0] = current[0] + (m * x)
    current[1] = current[1] + (m * y)
for i in current:
    print(i, end=" ")