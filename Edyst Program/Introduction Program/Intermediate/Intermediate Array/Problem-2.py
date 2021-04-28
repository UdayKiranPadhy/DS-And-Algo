# Chakravyuha

"""
During the battle of Mahabharat, when Arjuna was far away in the battlefield, 
Guru Drona made a Chakravyuha formation of the Kaurava army to capture Yudhisthir Maharaj. 
Abhimanyu, young son of Arjuna was the only one amongst the remaining Pandava army who knew 
how to crack the Chakravyuha. He took it upon himself to take the battle to the enemies.
Abhimanyu knew how to get power points when cracking the Chakravyuha. 
So great was his prowess that rest of the Pandava army could not keep pace with his advances. 
Worried at the rest of the army falling behind, Yudhisthir Maharaj needs your help to track of 
Abhimanyu’s advances. Write a program that tracks how many power points Abhimanyu has collected 
and also uncover his trail

A Chakravyuha is a wheel-like formation.

A Chakravyuha has a very well-defined co-ordinate system. 
Each point on the co-ordinate system is manned by a certain unit of the army. 
The Commander-In-Chief is always located at the center of the army to better co-ordinate his forces. 
The only way to crack the Chakravyuha is to defeat the units in sequential order.

A Sequential order of units differs structurally based on the radius of the Chakra. 
The radius can be thought of as length or breadth of the matrix depicted above. 
The structure i.e. placement of units in sequential order is as shown below.

1  2  3  4  5 
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

The entry point of the Chakravyuha is always at the (0,0) co-ordinate of the matrix above. 
This is where the 1st army unit guards. From (0,0) i.e. 1st unit Abhimanyu has to march 
towards the center at (2,2) where the 25th i.e. the last of the enemy army unit guards. 
Remember that he has to proceed by destroying the units in sequential fashion. 
After destroying the first unit, Abhimanyu gets a power point. 
Thereafter, he gets one after destroying army units which are multiples of 11. 
You should also be a in a position to tell Yudhisthir Maharaj the location at which Abhimanyu 
collected his power points.

Input Format
First line of input will be length as well as breadth of the army units, say N

Output Format
Print NxN matrix depicting the placement of army units, with unit numbers delimited by (\t) Tab character
Print Total power points collected
Print coordinates of power points collected in sequential fashion (one per line)
Constraints
0 < N <=100
Sample Input & Output
Input

2
Output

1 2
4 3
Total Power points : 1
(0,0)
Input

5
Output

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
Total Power points : 3
(0,0)
(4,2)
(3,2)
"""

n = int(input())
# n = 5
left, right, top, bottom = 0, n - 1, 0, n - 1
matrix = [[0 for i in range(n)] for j in range(n)]
current_count = 1
points = []
points.append([0, 0])
while (left <= right) & (top <= bottom):
    # Traverse Right
    for i in range(left, right + 1):
        matrix[top][i] = current_count
        if current_count % 11 == 0:
            points.append([top, i])
        current_count += 1
    top += 1

    # Traverse Down (Top to Bottom)
    for i in range(top, bottom + 1):
        matrix[i][right] = current_count
        if current_count % 11 == 0:
            points.append([i, right])
        current_count += 1
    right -= 1

    # Traverse Left
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = current_count
        if current_count % 11 == 0:
            points.append([bottom, i])
        current_count += 1
    bottom -= 1

    # Traverse Up (Bottom to Up)
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = current_count
        if current_count % 11 == 0:
            points.append([i, left])
        current_count += 1
    left += 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
print("Total Power points : " + str(len(points)))
for i in points:
    print("(" + str(i[0]) + "," + str(i[1]) + ")")
