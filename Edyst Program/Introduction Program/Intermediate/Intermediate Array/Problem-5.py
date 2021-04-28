# Min XOR Value

"""
Given an array of N integers, find the pair of integers in the array which have minimum XOR value. 
Report the minimum XOR value.

Examples :
Input
0 4 3 9
Output
3 (0 XOR 3)
Input
0 8 7 10
Output
2 (8 XOR 10)

Constraints:
2 <= N <= 100 000
0 <= A[i] <= 1 000 000 000
"""

# Theory
"""
Min XOR Value
Let us understand bit manipulation by exploring a problem. The problem is called Min XOR Value.

The problem states:

Given an array of N integers, find the pair of integers in the array which have minimum XOR value. Return the minimum XOR value.

As we have learned so far, no matter what, we should always start with the brute force solution. It might not be the most optimized, but it will help us find the answer.

Brute Force solution
In the brute force solution, we iterate through every possible pair and update the minimum XOR value when we find a lesser value.

Our pseudo-code for that:

min = 0
    for i: 0 to N
        for j: i+1 to N
            if A[i] ^ A[j] < min
                min = A[i] ^ A[j]
return min
As we can see, the above solution will run in O(n^2) time.

To get a more efficient solution, let’s go deeper into the XOR function.

Exploring XOR
Let us say we are taking the XOR of 2 pairs

A^B, A^C

And it is given that, A > B > C.

Then, can we make any conclusions about A^B and A^C. is A^B > A^C? or is A^B < A^C?

Let’s look at the nature of XOR to understand that.

Let’s say we have
A = …00000XXXX
B = …00000XXXX
C = …00000XXXX

Since B is closer to A than C, we are going to have a bit set closer to the left of B, than in C.

That is, a more significant bit of B will be set as compared to C.

Let’s understand what that means, with an example:

A = 10111 (23)
B = 10001 (17)
C = 01001 (9)

Since the more significant bit of B is set as compared to C, the resultant XOR will be of a lesser value because the the XOR will unset that particular bit.

Thus, if we were to check the values of XOR for a particular number, we need NOT check all the XOR pairs.

Instead, we only need to check for the number closest to it.

How do we do that?

We can simply sort the array! The array sorting happens in O(nlogn) time. Then we only consider those pairs of numbers that are adjacent to each other.

Efficient Approach
The pseudo-code for the same is:

sort(A) //O(nlogn)
min = 0
    for i: 0 to N-1 // O(n)
        if (A[i] ^ A[i+1] < min)
            min  = A[i] ^ A[i+1]
return min
The above approach is O(nlogn).
"""

list1 = list(map(int, input().split()))
list1.sort()
list2 = []
for i in range(len(list1) - 1):
    list2.append(list1[i] ^ list1[i + 1])
mini = 9999999
mini_pos = 0
for i in range(len(list2)):
    if list2[i] < mini:
        mini = list2[i]
        mini_pos = i
print(mini)