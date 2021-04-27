"""
Given a number n, the task is to find the XOR from 1 to n. 

Examples :
Input : n = 6
Output : 7
1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6  = 7

Input : n = 7
Output : 0
1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 = 0

"""
# Method 1 (Naive Approach): 
# 1- Initialize result as 0. 
# 1- Traverse all numbers from 1 to n. 
# 2- Do XOR of numbers one by one with result. 
# 3- At the end, return result.

# Method 2 (Efficient method) : 
# 1- Find the remainder of n by moduling it with 4. 
# 2- If rem = 0, then xor will be same as n. 
# 3- If rem = 1, then xor will be 1. 
# 4- If rem = 2, then xor will be n+1. 
# 5- If rem = 3 ,then xor will be 0.

def computeXOR(n) :
    # if n is multiple of 4
    if n % 4 == 0 :
        return n
 
    # If n % 4 gives remainder 1
    if n % 4 == 1 :
        return 1
 
    # If n%4 gives remainder 2
    if n % 4 == 2 :
        return n + 1
 
    # If n%4 gives remainder 3
    return 0

# Time Complexity is O(1)


"""
How does this work? 
When we do XOR of numbers, we get 0 as XOR value just before a multiple of 4. 
This keeps repeating before every multiple of 4. 
 

Number Binary-Repr  XOR-from-1-to-n
1         1           [0001]
2        10           [0011]
3        11           [0000]  <----- We get a 0
4       100           [0100]  <----- Equals to n
5       101           [0001]
6       110           [0111]
7       111           [0000]  <----- We get 0
8      1000           [1000]  <----- Equals to n
9      1001           [0001]
10     1010           [1011]
11     1011           [0000] <------ We get 0
12     1100           [1100] <------ Equals to n
"""