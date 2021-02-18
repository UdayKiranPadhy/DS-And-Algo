"""
Count the triplets 
https://practice.geeksforgeeks.org/problems/count-the-triplets4615/1
Easy 
Given an array of distinct integers. 
The task is to count all the triplets such that sum of two elements equals 
the third element.
 
Example 1:

Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: 2
Explanation: There are 2 triplets: 
1 + 2 = 3 and 3 +2 = 5 
â€‹Example 2:

Input: 
N = 3
arr[] = {2, 3, 4}
Output: 0
Explanation: No such triplet exits
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countTriplet() which takes the array arr[] and N as inputs and returns the triplet count

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 103
1 ≤ arr[i] ≤ 105

Company Tags
 Amazon Arcesium
Topic Tags
 Sorting Two-pointer-algorithm
"""

# My Trail :- Really Fucked up my self when seeing the solution not getting accepted
class Solution:
	def countTriplet(self, arr, n):
	    count=0
		for i in range(len(arr)):
			for j in range(i+1,len(arr)):
		        if (arr[i] + arr[j]) in arr:
		            count+=1
		return count


# Correct Answer
"""
1. Sort the given array, 
then the problem reduces to find the triplet where two numbers giving sum X.
"""
# Hint-2
"""
2. Try two pointer algorithm
    Step1: Maintain two pointer one starting from 0 and other one from n-2.
    Step2: Check if sum of two such elements equal to the (n-1)th element of array if so then increase count and increment one pointer ahead by 1 and decerement other pointer by 1.
    Step3: If sum is less, then move starting pointer ahead only
    Step4: if sum is more, then decrement end pointer by 1 only.
"""

# Code
"""
class Solution{
public:
	int countTriplet(int arr[], int n)
	{
		sort(arr, arr + n); 
		int  ans = 0;

		for (int i = n - 1; i >= 0; i--)
		{
			int j = 0;
			int k = i - 1;
			while (j < k)
			{
				if(arr[i] == arr[j] + arr[k])
				{
					ans++;
					j++;
					k--;
				}
				else if (arr[i] > arr[j] + arr[k])
					j++;
				else
					k--;
			}
		}

		return ans;
	}
	 
};
"""