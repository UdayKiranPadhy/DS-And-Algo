"""
Problem Statement : https://codeforces.com/contest/1525/problem/C

C. Robot Collisions
time limit per test 2 seconds
memory limit per test 256 megabytes
inputstandard input
outputstandard output

There are n robots driving along an OX axis. There are also two walls: 
one is at coordinate 0 and one is at coordinate m.

The i-th robot starts at an integer coordinate xi (0<xi<m) and moves either 
left (towards the 0) or right with the speed of 1 unit per second. No two 
robots start at the same coordinate.

Whenever a robot reaches a wall, it turns around instantly and continues his 
ride in the opposite direction with the same speed.

Whenever several robots meet at the same integer coordinate, they collide and 
explode into dust. Once a robot has exploded, it doesn't collide with any other 
robot. Note that if several robots meet at a non-integer coordinate, nothing happens.

For each robot find out if it ever explodes and print the time of explosion 
if it happens and −1 otherwise.

Input
The first line contains a single integer t (1≤t≤1000) — the number of testcases.

Then the descriptions of t testcases follow.

The first line of each testcase contains two integers n and m (1≤n≤3⋅105; 2≤m≤108) — 
the number of robots and the coordinate of the right wall.

The second line of each testcase contains n integers x1,x2,…,xn (0<xi<m) — the 
starting coordinates of the robots.

The third line of each testcase contains n space-separated characters 'L' or 'R' — the 
starting directions of the robots ('L' stands for left and 'R' stands for right).

All coordinates xi in the testcase are distinct.

The sum of n over all testcases doesn't exceed 3⋅105.

Output
For each testcase print n integers — for the i-th robot output the 
time it explodes at if it does and −1 otherwise.

Example
input
5
7 12
1 2 3 4 9 10 11
R R L L R R R
2 10
1 6
R R
2 10
1 3
L L
1 10
5
R
7 8
6 1 7 2 3 5 4
R L R L L L L
output
1 1 1 1 2 -1 2 
-1 -1 
2 2 
-1 
-1 2 7 3 2 7 3 
Note

For Case 1
Notice that robots 2 and 3 don't collide because they meet at the same point 2.5, 
which is not integer.

After second 3 robot 6 just drive infinitely because there's no robot to collide with.

"""

# Editoral
"""
Notice that the robots that start at even coordinates can never collide with the 
robots that start at odd coordinates. You can see that if a robot starts at an 
even coordinate, it'll be at an even coordinate on an even second and at an odd 
coordinate on an odd second.

Thus, we'll solve the even and the odd cases separately.

Sort the robots by their starting coordinate. Apparently, that step was an 
inconvenience for some of you. There is a common trick that can help you to 
implement that. Create a separate array of integer indices 1,2,…,n and sort 
them with a comparator that looks up the value by indices provided to tell 
the order. This gives you the order of elements and doesn't require you to 
modify the original data in any way.

Consider the task without reflections of the wall. Take a look at the first 
robot. If it goes to the left, then nothing ever happens to it. Otherwise, 
remember that it goes to the right. Look at the next one. If it goes to the 
left, then it can collide with the first one if that went to the right. 
Otherwise, remember that it also goes to the right. Now for the third one. 
If this one goes to the left, who does it collide with? Obviously, the 
rightmost alive robot that goes to the right.

So the idea is to keep a stack of the alive robots. If a robot goes to the 
left, then check if the stack is empty. If it isn't, then the top of the 
stack robot is the one who will collide with it. Pop it from the stack, 
since it explodes. If a robot goes to the right, simply push it to the stack. 
The time of the collision is just the distance between the robots divided by 2.

If there are robots left in the stack after every robot is processed, 
then they all go to the right together, so they never collide.

What changes when the reflections are introduced?

Almost nothing, actually. Well, now if the stack is empty and a robot goes 
to the left, then it behaves as a one going to the right. You can reflect 
the part of the way from its start to the wall. Just say that instead of 
starting at some x going to the left, it starts at −x going to the right. 
Since there's no one alive to the left of him initially, that will change 
nothing. That −x should be used for computing the collision time.

However, the final robots in the stack also act differently. First, the 
top of the stack robots reflects off the wall and collides with the second 
on the stack one. Then the third and the fourth and so on. So you can pop 
them in pairs until 0 or 1 are left.

The coordinate reflection trick can be used here as well. Imagine that the 
top of the stack starts at m+(m−x) and goes to the left instead of starting 
in x going to the right. For the same reason it changes nothing.

Overall complexity: O(nlogn).
"""

# 7 12
# 1 2 3 4 9 10 11
# R R L L R R R


def partner(robots):
    robots.sort()  # Sorting based on Co-ordinates
    partnerships = []  # Will Store which robot will colide with other robot
    stack = []  # Used for Storing Robots going to right
    for robot in robots:
        # If the robot is moving right then append to the list
        if len(stack) == 0 or robot[1] == "R":
            stack.append(robot)
        else:
            # Since robot is going to left pop a robot which is moving to right
            poppedRobot = stack.pop()
            # Make them A pair
            partnerships.append((poppedRobot, robot))
    # Make pairs of remaining robots
    while len(stack) > 1:
        poppedRobot1 = stack.pop()
        poppedRobot2 = stack.pop()
        partnerships.append((poppedRobot2, poppedRobot1))

    return partnerships


NoOfTestCases = int(input())
for t in range(NoOfTestCases):
    n, m = [int(i) for i in input().strip().split(" ")]
    co_ordinates = [int(x) for x in input().strip().split(" ")]
    directions = [x for x in input().split(" ")]
    robots = list(zip(co_ordinates, directions, range(n)))
    odd = []
    even = []
    for robot in robots:
        if robot[0] % 2 == 0:
            even.append(robot)
        else:
            odd.append(robot)

    partnerships = partner(even) + partner(odd)
    # [((2, 'R', 1), (4, 'L', 3)), ((1, 'R', 0), (3, 'L', 2)), ((9, 'R', 4), (11, 'R', 6))]
    distances = [-1] * n
    for a, b in partnerships:
        if a[1] == "R" and b[1] == "L":
            distance = (b[0] - a[0]) // 2
        elif a[1] == "L" and b[1] == "L":
            distance = (b[0] + a[0]) // 2
        elif a[1] == "R" and b[1] == "R":
            distance = (2 * m - (a[0] + b[0])) // 2
        else:
            distance = (2 * m + a[0] - b[0]) // 2

        distances[a[2]] = distance
        distances[b[2]] = distance

    print(*distances)
