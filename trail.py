import io
import os
import sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
# input = sys.stdin.readline


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


NoOfTestCases = int(input() )
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
