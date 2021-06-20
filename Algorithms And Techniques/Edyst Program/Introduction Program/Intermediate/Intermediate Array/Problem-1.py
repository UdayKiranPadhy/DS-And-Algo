# Efficient Janitor

"""
The janitor of a high school is insanely efficient. By the end of the day, 
all of the waster from the trash cans in the school has been shifted into plastic bags which 
can carry waster weighting between 1.01 pounds and 3.00 pounds.

All of the plastic bags must be dumped into the trash cans outside the school. 
The janitor can carry at most 3.00 pounds at once.

One trip is described as selecting a few bags which together don't weigh more than 3.00 pounds, 
dumping them in the outdoor trash can and returning to the school. 
The janitor wants to make minimum number of trips to the outdoor trash can.

Given the number of plastic bags, n and the weights of each bag, 
determine the minimum number of trips if the janitor selects bags in the optimal way.

For example, given n=5, plastic bags weighing weights [1.01, 1.99, 2.5, 1.5, 1.01], 
the janitor can carry all of the trash out in 3 trips: [1.01+1.99, 2.5, 1.5+1.01]

Constraints

1 <= n <= 1000
1.01 <= weight <= 3.0
"""


"""
Theory I learnt:-
Some times looking at the problem itself think about sorting it out at the first instant.
We cant solve this problem without taking the indeices of the list 
We cant solve the problem by taking element wise in the "i" in for i in list
There are two methods 
1)Similar to bubble sort add two adjcent element of sorted weighted list and check weather its less than the constraints
2)Compare 1st and last element of the list and add the trips
"""

# Wrong Method
"""
t = int(input())
trip = 0
w = list(map(float, input().split()))
w.sort()
for i in w:
    if i > 1.99:
        trip += 1
        continue
"""

# Method 1
t = int(input())
l = list(map(float, input().split(" ")))
l.sort()
trip = 0
i, j = 0, len(l) - 1
while i <= j:
    trip += 1
    if l[i] + l[j] <= 3.0:
        i += 1
    j -= 1
print(trip)


# Method 2
n = int(input())
a = []
for i in range(n):
    x = float(input())
    a.append(x)
j, trips = 0, 0
while j < len(a) - 1:
    if a[j] + a[j + 1] <= 3.00:
        trips += 1
        j += 2
        if j == len(a) - 1:
            trips += 1
            break
        else:
            continue
    else:
        trips += 1
        j += 1
print(trips)


# Similar problem
"""
https://leetcode.com/problems/boats-to-save-people/

The i-th person has weight people[i], and each boat can carry a maximum weight of limit.

Each boat carries at most 2 people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.  (It is guaranteed each person can be carried by a boat.)

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
Note:

1 <= people.length <= 50000
1 <= people[i] <= limit <= 30000

"""