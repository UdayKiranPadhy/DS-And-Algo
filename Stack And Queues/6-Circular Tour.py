"""
The problem “Find the First Circular Tour that visits all the Petrol Pumps” states that there are N petrol pumps on a circular road. Given the petrol that every petrol pump has and the amount of petrol required to cover the distance between two petrol pumps. So you need to find the first petrol pump where a truck starts and can complete the circle.
The input format is as, {x, y}, where x is the petrol that the petrol pump has and y is the fuel needed to reach from this petrol pump to next petrol pump.
If there is no possible tour, output -1.

Examples
{{5, 3}, {2, 7}, {11, 2}, {8, 9}}
3

{{1, 1}, {2, 2}, {1, 2}, {3, 1}}
4
{{2, 3}, {4, 5}, {1, 1}, {3, 3}}
-1
"""


# Naive Approach
"""
One by one consider every petrol pump as starting point. If there exists a possibly valid tour. 
Return the current petrol pump number. Else if there is no possible tour from any petrol pump, return -1.

1)Run a loop from 1 to n, this loop consider the ith petrol pump as the starting point.
2)Initialize a variable currFuel as 0, which represents the amount of petrol in the truck.
3)To travel from jth petrol pump to (j + 1)th petrol pump, (fuel[j] – cost[j]) amount of fuel is added to currFuel.
4)From the ith petrol pump start traveling ahead in the circle and add the extra fuel(fuel[j] – cost[j]) at every step, repeat this process while currFuel >= 0.
5)If the truck is able to traverse through all the n petrol pumps, return i. Else continue for next i.
6)If there is no i for which the truck can traverse the whole circle, return -1.
"""


def CircularTour(fuel, distance, units):
    for i in range(units):
        curr_petrol = 0
        travelled = 0
        while curr_petrol >= 0 and travelled < units:
            curr_petrol = (
                curr_petrol
                + fuel[(i + travelled) % units]
                - distance[(i + travelled) % units]
            )  # Here %units is for :- if i = 3 and travelled is 2 then it comes list index out of range so we take reminder
            travelled += 1
        if travelled == units and curr_petrol >= 0:
            return i + 1
            break
    else:
        return -1


print(CircularTour([5, 2, 11, 8], [3, 7, 2, 9], 4))
print(CircularTour([1, 2, 1, 3], [1, 2, 2, 1], 4))
print(CircularTour([2, 4, 1, 3], [3, 5, 1, 3], 4))

# Complexity Analysis
"""
Time Complexity
O(n2), is the time complexity. Where N is the number of petrol pumps in the given input. 
Here we have polynomial complexity because we have considered each petrol pump as starting point. 
After making each petrol pump as starting we made a complete tour. 
And checked whether during the tour the petrol tank gets empty. 
So we had N starting points and then each starting point had N-1 petrol pumps to cover. Thus the time complexity is O(N^2).
"""
"""
Space Complexity
O(1), here we haven’t saved any information which was required for each element simultaneously. 
And thus we have not used much space. We have used a constant number of variables which made the space complexity constant.
"""

# Optimal Approach
# Keep two variables named surplus and difficiet and if surplus becomes less than zero increment to difficiet , increment start to i, make sum to zero.
# https://youtu.be/nTKdYm_5-ZY
# https://youtu.be/nTKdYm_5-ZY?t=514
def CircularTour2(fuels, distance, n):
    start = 0
    diff = 0
    sum = 0
    for i in range(n):
        sum = sum + fuels[i] - distance[i]
        if sum < 0:
            start = i + 1
            diff += sum
            sum = 0
    if sum + diff >= 0:
        return start + 1
    else:
        return -1


print(CircularTour2([5, 2, 11, 8], [3, 7, 2, 9], 4))
print(CircularTour2([1, 2, 1, 3], [1, 2, 2, 1], 4))
print(CircularTour2([2, 4, 1, 3], [3, 5, 1, 3], 4))