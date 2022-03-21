"""
Minimum Platforms 
Medium
Given arrival and departure times of all trains that reach a railway station. 
Find the minimum number of platforms required for the railway station so that 
no train is kept waiting.
Consider that all the trains arrive on the same day and leave on the same day. 
Arrival and departure time can never be the same for a train but we can have 
arrival time of one train equal to departure time of the other. 
At any given instance of time, same platform can not be used for both 
departure of a train and arrival of another train. In such cases, 
we need different platforms,

 

Example 1:

Input: N = 6 
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
Output: 3
Explanation: 
Minimum 3 platforms are required to 
safely arrive and depart all trains.
Example 2:

Input: N = 3
arr[] = {0900, 1100, 1235}
dep[] = {1000, 1200, 1240}
Output: 1
Explanation: Only 1 platform is required to 
safely manage the arrival and departure 
of all trains. 
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function findPlatform() which takes the array arr[] (denoting the arrival times), array dep[] (denoting the departure times) and the size of the array as inputs and returns the minimum number of platforms required at the railway station such that no train waits.

Note: Time intervals are in the 24-hour format(HHMM) , where the first two characters represent hour (between 00 to 23 ) and the last two characters represent minutes (between 00 to 59).

 

Expected Time Complexity: O(nLogn)
Expected Auxiliary Space: O(n)

Constraints:
1 <= N <= 1000
1 <= A[i] < D[i] <= 2359

Company Tags
 Amazon Boomerang Commerce D-E-Shaw Hike Paytm Walmart Zillious Microsoft
Topic Tags
 Arrays Greedy 2-Pointer
Related Course
"""

# Approch 1
"""
Naive Solution: 

Approach: The idea is to take every interval one by one and find the number of 
intervals that overlap with it. Keep track of the maximum number of intervals 
that overlap with an interval. Finally, return the maximum value.

Algorithm: 
Run two nested loops the outer loop from start to end and inner loop from i+1 to end.
For every iteration of outer loop find the count of intervals that intersect with the current interval.
Update the answer with maximum count of overlap in each iteration of outer loop.
Print the answer.
"""
"""
int plat_needed = 1, result = 1;
    int i = 1, j = 0;
 
    // run a nested  loop to find overlap
    for (int i = 0; i < n; i++) {
        // minimum platform
        plat_needed = 1;
 
        for (int j = i + 1; j < n; j++) {
            // check for overlap
            if ((arr[i] >= arr[j] && arr[i] <= dep[j]) || 
           (arr[j] >= arr[i] && arr[j] <= dep[i]))
                plat_needed++;
        }
 
        // update result
        result = max(result, plat_needed);
"""

"""
Complexity Analysis: 

Time Complexity: O(n^2). 
Two nested loops traverse the array, so the time complexity is O(n^2).
Space Complexity: O(1). 
As no extra space is required.
"""


# Efficient Solution:
"""
Approach: The idea is to consider all events in sorted order. 
Once the events are in sorted order, trace the number of trains at any time 
keeping track of trains that have arrived, but not departed.
For example consider the above example. 

arr[]  = {9:00,  9:40, 9:50,  11:00, 15:00, 18:00}
dep[]  = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00}

All events are sorted by time.
Total platforms at any time can be obtained by
subtracting total departures from total arrivals
by that time.

 Time      Event Type     Total Platforms Needed 
                               at this Time                               
 9:00       Arrival                  1
 9:10       Departure                0
 9:40       Arrival                  1
 9:50       Arrival                  2
 11:00      Arrival                  3 
 11:20      Departure                2
 11:30      Departure                1
 12:00      Departure                0
 15:00      Arrival                  1
 18:00      Arrival                  2 
 19:00      Departure                1
 20:00      Departure                0

Minimum Platforms needed on railway station 
= Maximum platforms needed at any time 
= 3
Note: This approach assumes that trains are arriving and departing on the same date. 
 

Algorithm:

Sort the arrival and departure time of trains.
Create two pointers i=0, and j=0 and a variable to store ans and 
current count plat
Run a loop while i<n and j<n and compare the ith element of arrival array 
and jth element of departure array.
if the arrival time is less than or equal to departure then one more platform 
is needed so increase the count, i.e. plat++ and increment i
Else if the arrival time greater than departure then one less platform 
is needed so decrease the count, i.e. plat– and increment j
Update the ans, i.e ans = max(ans, plat).

Implementation: This doesn’t create a single sorted list of all events, rather 
it individually sorts arr[] and dep[] arrays, and then uses merge process 
of merge sort to process them together as a single sorted array. 

"""
def minimumPlatform(n,arr,dep):
    '''
    :param n: number of activities
    :param arr: arrival time of trains
    :param dep: corresponding departure time of trains
    :return: Integer, minimum number of platforms needed
    '''
    arr.sort()
    dep.sort()

    i=0
    j=0
    max_platform=-1
    curr_platform=0
    while i < n and j <n:
        if (arr[i]<=dep[j]):
            curr_platform+=1
            i +=1
        elif (arr[i]>dep[j]):
            curr_platform -=1
            j+=1
        max_platform=max(curr_platform,max_platform)
    return max_platform

print(minimumPlatform(6,[900, 940, 950, 1100, 1500, 1800],[910, 1200, 1120, 1130, 1900, 2000]))
