"""
You are given n activities with their start and finish times.
Select the maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time.
"""

# Example 1 : Consider the following 3 activities sorted by
# by finish time.
#      start[]  =  {10, 12, 20};
#      finish[] =  {20, 25, 30};
# A person can perform at most two activities. The
# maximum set of activities that can be executed
# is {0, 2} [ These are indexes in start[] and
# finish[] ]

# Example 2 : Consider the following 6 activities
# sorted by by finish time.
#      start[]  =  {1, 3, 0, 5, 8, 5};
#      finish[] =  {2, 4, 6, 7, 9, 9};
# A person can perform at most four activities. The
# maximum set of activities that can be executed
# is {0, 1, 3, 4} [ These are indexes in start[] and
# finish[] ]

# Procedure: -
# 1) Sort the activities according to their finishing time
# 2) Select the first activity from the sorted array and print it.
# 3) Do following for remaining activities in the sorted array.
# …….a) If the start time of this activity is greater than or equal to the finish time of
#     previously selected activity then select this activity and print it.


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