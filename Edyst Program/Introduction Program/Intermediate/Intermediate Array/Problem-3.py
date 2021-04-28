# Bottle Necks

"""
There are N bottles. ith bottle has A[i] radius. Once a bottle is enclosed inside another bottle, 
it ceases to be visible. Minimize the number of visible bottles.

You can put ith bottle into jth bottle if following condition is fulfilled:
ith bottle itself is not enclosed in another bottle.
jth bottle does not enclose any other bottle.
Radius of bottle i is smaller than bottle j (i.e. A[i] < A[j]).

Constraints
1 <= N <= 100000
1 <= A[i] <= 1018

Input Format
First line contains T, the number of test cases. For each test case:
First line contains a single integer N denoting the number of bottles
Second line contains N space separated integers, ith integer denoting the radius of ith bottle.
(1 <= i <= N)

Output
Minimum number of visible bottles after all the operations
Example 
Input
2
8
1 1 2 3 4 5 5 4
5
5 7 1 2 4

Output
2
1

Explanation
In the first case:
1st bottle can be kept in 3 rd one 1-->2 , which makes following bottles visible [1,2,3,4,5,5,4]
Similarly after following operations, the following will be the corresponding visible bottles
Operation	Visible Bottles
2 --> 3	    [1,3,4,5,5,4]
3 --> 4	    [1,4,5,5,4]
4 --> 5	    [1,5,5,4]
1 --> 4	    [5,5,4]
4 --> 5	    [5,5]
Finally there are 2 bottles which are visible. Hence, the answer is 2
In the second case, we can follow the operations: 1 -> 2 -> 4 -> 5 -> 7
"""

# My Trail
"""
1st Sort the array and follow Longest Increaing Subsequence proceduce some thing like that.
"""

# Approach
"""
Approach: If you carefully observe, you will find that the number of minimum visible 
bottles will be equal to the maximum number of repeated bottles. 
Here intuition is, as these repeated bottles cannot be fit in single bigger bottle 
hence we require at least as many bigger bottles as the number of repeated bottles.
"""

t = int(input())
l = []
for i in range(t):
    int1 = int(input())
    l.append(list(map(int, input().split(" "))))
for i in l:
    i.sort()
    max_rep = 1
    cur_max = 1
    pre_max = 0
    for j in range(len(i) - 1):
        if i[j] == i[j + 1] and pre_max == i[j]:
            cur_max += 1
            if cur_max > max_rep:
                max_rep = cur_max
            continue
        if i[j] == i[j + 1]:
            cur_max = 2
            pre_max = i[j]
            if cur_max > max_rep:
                max_rep = cur_max
    print(max_rep)