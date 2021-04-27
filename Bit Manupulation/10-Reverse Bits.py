"""
Reverse Bits 
Easy
Given a 32 bit number X, reverse its binary form and print the answer in 
decimal.

Example 1:
Input:
X = 1
Output:
2147483648 
Explanation:
Binary of 1 in 32 bits representation-
00000000000000000000000000000001
Reversing the binary form we get, 
10000000000000000000000000000000,
whose decimal value is 2147483648.

Example 2:
Input:
X = 5
Output:
2684354560 
Explanation:
Binary of 5 in 32 bits representation-
00000000000000000000000000000101
Reversing the binary form we get, 
10100000000000000000000000000000,
whose decimal value is 2684354560.

Your Task:
You don't need to read input or print anything. Your task is to complete 
the function reversedBits() which takes an Integer X as input and returns 
the answer.

Expected Time Complexity: O(log(X))
Expected Auxiliary Space: O(1)

Constraints:
0 <= X < 232

Company Tags
 Amazon Cisco HCL Nvidia Qualcomm
Topic Tags
 Bit Magic Mathematical
"""
# https://practice.geeksforgeeks.org/problems/reverse-bits3556/1#

def reversedBits(X):
    bin_x = bin(X).lstrip("0b")
    bin_x = bin_x.rjust(32, "0")
    print(bin_x)
    print(int(bin_x[::-1], 2))


reversedBits(5)