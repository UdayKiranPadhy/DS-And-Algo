"""

Maximum circular subarray sum

Given n numbers (both +ve and -ve), arranged in a circle, 
find the maximum sum of consecutive number. 
Examples: 

Input: a[] = {8, -8, 9, -9, 10, -11, 12}
Output: 22 (12 + 8 - 8 + 9 - 9 + 10)

Input: a[] = {10, -3, -4, 7, 6, 5, -4, -1} 
Output:  23 (7 + 6 + 5 - 4 -1 + 10) 

Input: a[] = {-1, 40, -14, 7, 6, 5, -4, -1}
Output: 52 (7 + 6 + 5 - 4 - 1 - 1 + 40)


"""

# my trail
"""
 There can be two cases for the maximum sum:

Case 1 (We get maximum sum using normal subarray) : The elements that 
contribute to the maximum sum are arranged such that no wrapping 
is there. Examples: {-10, 2, -1, 5}, {-2, 4, -1, 4, -1}. In this case, 
Kadane's Algorithm will produce the result.

Case 2 (We get maximum sum using both corner elements): The elements 
which contribute to the maximum sum are arranged such that wrapping is 
there. Examples: {10, -12, 11}, {12, -5, 4, -8, 11}.In this case, 
we change wrapping to non-wrapping. Let us see how. Wrapping of 
contributing elements implies non-wrapping of non-contributing elements, 
so find out the sum of non-contributing elements and subtract this sum 
from the total sum. To find out the sum of non contributing, invert the 
sign of each element and then run Kadane’s algorithm. 
Our array is like a ring and we have to eliminate the maximum continuous 
negative that implies maximum continuous positive in the inverted arrays. 
Finally, we compare the sum obtained by both cases and return the 
maximum of the two sums.
"""


def circularSubarraySum(arr, n):
    sum_of_array = sum(arr)
    gg = kadanes(arr)
    for i in range(len(arr)):
        arr[i] = -arr[i]
    non_contributing = kadanes(arr)
    return max(gg, sum_of_array + non_contributing)



def kadanes(array):
    curr_sum = 0
    max_sum = -99999999999
    for i in range(len(array)):
        curr_sum += array[i]
        if curr_sum < 0:
            curr_sum = array[i]
        max_sum = max(curr_sum, max_sum)
    return max_sum


"""

Actual Solution

def kadane(arr,n):
	max_so_far = 0
	max_ending_here = 0
	for i in range(0, n):
	    #Storing max sum till current index.
		max_ending_here = max_ending_here + arr[i]
		
		#If max sum till current index is negative, we update it to 0.
		if (max_ending_here < 0):
			max_ending_here = 0
			
		#Storing the max sum so far.
		if (max_so_far < max_ending_here):
			max_so_far = max_ending_here
	return max_so_far

#Function to find maximum circular subarray sum.
def circularSubarraySum(arr,n):
    
    count =0
    maxx =-sys.maxsize -1 
    for i in range(0, n):
        #Storing the maximum element in the array.
        if(arr[i] > maxx):
            maxx = arr[i]
        #Counting total number of negative numbers in the array.
        if(arr[i] < 0):
            count=count+1
                
    if(count == n):
        return maxx

	#Case 1:We get the maximum sum using standard Kadane's algorithm.
    max_kadane = kadane(arr,n)

	#Case 2:We now find the maximum sum that includes corner elements.
    max_wrap = 0
    for i in range(0, n):
	    #Calculating total sum of array elements.
	    max_wrap += arr[i]
		#Inverting the sign of array elements.
	    arr[i] = -arr[i]

	#Maximum sum with corner elements will be: 
	#Total sum of array elements-(-max subarray sum after changing 
	#sign of array elements).  
    max_wrap = max_wrap + kadane(arr,n)

	#The maximum circular sum will be maximum of two sums.
    if max_wrap > max_kadane:
	    return max_wrap
    else:
	    return max_kadane
       

"""
