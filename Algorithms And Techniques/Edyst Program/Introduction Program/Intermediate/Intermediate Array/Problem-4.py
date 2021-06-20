# Crest And Trough

"""
Given an array of n elements, find out all the crests and troughs along with their lengths. 
Find the absolute difference between the indexes of  longest and shortest crests as well as 
troughs and display the maximum of both.

An element is said to be crest if both it's previous and next elements are less than the current element.
An element is said to be trough if both it's previous and next elements are greater than the current element.
Note: The first and last elements are neither crests nor troughs.

In case of multiple occurrences of shortest crest/trough consider the left most one as shortest and 
right most one as longest.

Print -1 if at least one crest and trough doesn't exist.

Try to finish the task using O(1) extra space and traversing the array only once.

Input Format

The first line contains an integer, t denoting the number of test cases.
The first line of each test case contains an integer, n denoting the size of the arr.
The second line of each test case contains n space-separated integers describing the elements of array.
Constraints

4<=n<=109
0<=arr[i]<=n
Output Format

For every test case print the required output in a new line.

Sample Input 0

1
8
3 6 2 8 9 5 10 1
Sample Output 0

2
Explanation 0

The crest with maximum length(length-->10-1=9) exists at index 6.
The crest with minimum length(length-->9-8=1) exists at index 4.
The trough with maximum length(length-->8-2=6) exists at index 2.
The trough with minimum length(length-->6-2=4) exists at index 2 (troughs with length 4 exists at two indexes 2 and 5, but take trough at index 2 as shortest trough as it is left most).

Print 2 as (difference between indexes of longest and shortest crests) 6-4 > 2-2 (difference between indexes of longest and shortest troughs).
"""
import sys

t = int(input())
list1 = []
for i in range(t):
    _ = int(input())
    list1.append(list(map(int, input().split())))
for l in list1:
    c_min, c_max = sys.maxsize, -sys.maxsize - 1
    c_min_pos, c_max_pos = 0, 0
    t_min, t_max = sys.maxsize, -sys.maxsize - 1
    t_min_pos, t_max_pos = 0, 0
    for i in range(1, len(l) - 1):
        if l[i - 1] < l[i] and l[i] > l[i + 1]:
            a = l[i] - l[i - 1]
            b = l[i] - l[i + 1]
            maxi = a if a > b else b
            mini = a if a < b else b
            if c_min > mini:
                c_min = mini
                c_min_pos = i
            if c_max < maxi:
                c_max = maxi
                c_max_pos = i
            # print(
            #     f"Crest at Location {i} is {l[i]} and the c_min value is {c_min} , cmax{c_max}"
            # )
        if l[i - 1] > l[i] and l[i] < l[i + 1]:
            a = l[i] - l[i - 1]
            b = l[i] - l[i + 1]
            maxi = a if a > b else b
            mini = a if a < b else b
            if t_min > mini:
                t_min = mini
                t_min_pos = i
            if t_max < maxi:
                t_max = maxi
                t_max_pos = i
            # print(
            #     f"Tough at Location {i} is {l[i]} and the t_min value is {t_min} , t_max {t_max}"
            # )
    if (c_max_pos == 0) or (t_max_pos == 0):
        print("-1")
    else:
        print(max(abs(c_max_pos - c_min_pos), abs(t_max_pos - t_min_pos)))
        
        
        
   








t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    max_c_position=0
    min_c_position=0
    max_t_position=0
    min_t_position=0
    max_crests=0
    min_crests=1000
    max_troughs=0
    min_troughs=1000
    #crests=max(l)
    
    for i in range(1,len(l)-1):
        if l[i]>l[i-1] and l[i]>l[i+1]:
            if max((l[i]-l[i-1]),(l[i]-l[i+1]))>max_crests:
                max_crests=max((l[i]-l[i-1]),(l[i]-l[i+1]))
                max_c_position=i
            if min((l[i]-l[i-1]),(l[i]-l[i+1]))<min_crests:
                min_crests=min((l[i]-l[i-1]),(l[i]-l[i+1]))
                min_c_position=i
            
        elif l[i]<l[i-1] and l[i]<l[i+1]:
            #print("hi")
            if max((l[i-1]-l[i]),(l[i+1]-l[i]))>max_troughs:
                #print("hello")
                max_troughs=max((l[i-1]-l[i]),(l[i+1]-l[i]))
                max_t_position=i
            if min((l[i-1]-l[i]),(l[i+1]-l[i]))<min_troughs:
                min_troughs=min((l[i-1]-l[i]),(l[i+1]-l[i]))
                min_t_position=i
    if max_c_position==0 and min_c_position==0 and max_t_position==0 and min_t_position==0:print("-1")
    else:
        x=abs((max_c_position)-(min_c_position))
        y=abs((max_t_position)-(min_t_position))
        if x>=y:print(x)
        elif y>x:print(y)
