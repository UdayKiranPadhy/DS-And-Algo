# Check pair with difference k
"""
Given an array A of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

Input Format
First line is number of test cases T. Following T lines contain:
N, followed by N integers of the array
The non-negative integer k
Output format
Print 1 if such a pair exists and 0 if it doesn’t.

Example
Input
1
3 1 3 5
4

Output:
1

Explaination:-
|1 - 5| = 4
"""

# Method
"""
Method 1: Brute Force
The simplest method is to run two loops, the outer loop picks the first element (smaller element) and the inner loop looks for the element picked by outer loop plus B.
Time complexity of this method is O(N2). This wil not work lets us look on an optimized method.

Method 2: Sorting + Binary Search
We can use sorting and Binary Search to improve time complexity to O(NLogN).

The first step is to sort the array in ascending order.
Once the array is sorted, traverse the array from left to right, and for each element A[i], binary search for A[i] + B in A[i+1..n-1]. If the element is found, return 1.
Both first and second steps take O(NLogN). So overall complexity is O(NLogN).
Time Complexity : O(NlogN + NlogN)

Method 3: Sorting + Two Pointers
The second step of the above algorithm can be improved to O(N). The first step remain same.
The idea for second step:

Take two index variables i and j, initialize them as 0 and 1 respectively.
Now run a linear loop. If A[j] – A[i] is smaller than B, we need to look for greater A[j], so increment j.
If A[j] – A[i] is greater than B, we need to look for greater A[i], so increment i.
Time Complexity : O(NlogN + N)

Methos 4: Hashing
Create an empty hash table HT. Traverse the array, use array elements as hash keys and enter them in HT.
Traverse the array again look for value B + A[i] in HT.
Time Complexity: O(N) if we use unordered_map



"""


# Approarch 1
"""
l = []
k = []
for i in range(int(input())):
    l.append(list(map(int, input().split())))
    k.append(int(input()))

for i, j in zip(l, k):
    i.sort()
    print(i)
    left_pointer = 0
    right_pointer = len(i) - 1
    for d in range(len(i)):
        print(f"Left Pointer {left_pointer}")
        print(f"Right Pointer {right_pointer}")
        print(f"Difference {abs(i[left_pointer] - i[right_pointer])}")
        if (left_pointer == len(i)) or (right_pointer == len(i)):
            print("0")
            break
        if abs(i[left_pointer] - i[right_pointer]) == j:
            print("1")
            break
        if abs(i[left_pointer] - i[right_pointer]) > j:
            left_pointer += 1
            continue
        if abs(i[left_pointer] - i[right_pointer]) < j:
            right_pointer -= 1
            continue
"""

# Approach 2
l = []
k = []
for i in range(int(input())):
    l.append(list(map(int, input().split())))
    k.append(int(input()))

for i, j in zip(l, k):
    i.sort()
    index = 1
    for g in i:
        if g + j in i[index:]:
            print("1")
            break
        index += 1
    else:
        print("0")

    # Approach 3
    def solve(self, A, B):
        set1 = set(A)
        for ele in set1:
            set1.remove(ele)
            if ele + B in set1:
                return 1
            set1.add(ele)
        return 0
