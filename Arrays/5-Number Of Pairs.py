"""
Number of pairs 

Given two arrays X and Y of positive integers, find the number of pairs 
such that xy > yx (raised to power of) where x is an element from X and y 
is an element from Y.

Example 1:

Input: 
M = 3, X[] = [2 1 6] 
N = 2, Y[] = [1 5]
Output: 3
Explanation: 
The pairs which follow x**y > y**x (** stands for power)are 
as such: 21 > 12,  25 > 52 and 61 > 16 .
Example 2:

Input: 
M = 4, X[] = [2 3 4 5]
N = 3, Y[] = [1 2 3]
Output: 5
Explanation: 
The pairs for the given input are 
21 > 12 , 31 > 13 , 32 > 23 , 41 > 14 , 
51 > 15 .


Expected Time Complexity: O((N + M)log(N)).
Expected Auxiliary Space: O(1).

https://practice.geeksforgeeks.org/problems/number-of-pairs-1587115620/1
"""



class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(a,b,M,N):


        