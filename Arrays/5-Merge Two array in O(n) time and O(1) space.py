"""
Merge Without Extra Space 
Hard 
Given two sorted arrays arr1[] and arr2[] of sizes N and M in non-decreasing order. 
Merge them in sorted order without using any extra space. 
Modify arr1 so that it contains the first N elements and modify arr2 so that 
it contains the last M elements. 

Example 1:
Input: 
N = 4, arr1[] = [1 3 5 7] 
M = 5, arr2[] = [0 2 6 8 9]
Output: 
arr1[] = [0 1 2 3]
arr2[] = [5 6 7 8 9]
Explanation:
After merging the two 
non-decreasing arrays, we get, 
0 1 2 3 5 6 7 8 9.

Example 2:
Input: 
N = 2, arr1[] = [10, 12] 
M = 3, arr2[] = [5 18 20]
Output: 
arr1[] = [5 10]
arr2[] = [12 18 20]
Explanation:
After merging two sorted arrays 
we get 5 10 12 18 20.


Your Task:
You don't need to read input or print anything. 
You only need to complete the function merge() that takes arr1, arr2, 
N and M as input parameters and modifies them in-place so that 
they look like the sorted merged array when concatenated.
 

Expected Time Complexity:  O((n+m) log(n+m))
Expected Auxilliary Space: O(1)
 

Constraints:
1 <= X, Y <= 5*10^4
0 <= arr1i, arr2i <= 10^9

Company Tags
 Amdocs Brocade Goldman Sachs Juniper Networks Linkedin Microsoft Quikr Snapdeal Synopsys Zoho
Topic Tags
 Mathematical Sorting
https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
"""


def merge(arr1, arr2):
    i = 0
    j = 0
    while j < len(arr2) and i < len(arr1):
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            temp = j
            while True:
                if temp + 1 < len(arr2):
                    if arr2[temp] > arr2[temp + 1]:
                        arr2[temp], arr2[temp + 1] = arr2[temp + 1], arr2[temp]
                        temp += 1
                    else:
                        break
                else:
                    break


arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]
merge(arr1, arr2)
print(arr1)
print(arr2)

# Hint 1
"""
How to solve this question in O(1) space.

Ever heard of Shell Sort..??? If not, first go through this - https://www.geeksforgeeks.org/shellsort/
We need to use a modification of shell sort over 2 sorted arrays, such that one array is just behind second array.

Now how to do that..???
"""

# Hint 2
"""
Partial solution:

Maintain 2 iterators i, j for 2 arrays. 
Calculate gap
First iterate the first array, and check for elements at index i and i + gap, and swap if second is smaller.
When i + gap will cross the last index of first array, the control will move on to second array.
So now iterate, for i in first array, and j in second array, till one stops.
But there are 2 more cases, to think about in this solution. Try yourself. Think Hard.
"""

# Hint 3
"""
Complete Solution

Continuing from previous hint, we need to consider the case, when gap comes more than size of first array, at start of iteration.
Then the iteration in second array should start from index gap - n (size of arr1), and not 0
Also, at end of iteration, when one of the iterators come to end, there are 2 cases
if j ends for second array, then the iteration ends
but, if i ends for first array, and second array is still left for iteration, then we need to iterate for second array, and check for elements at j and j + gap, and swap accordingly
This is the complete solution with all cases.
"""

# https://youtu.be/hVl2b3bLzBw

# Python
def nextGap(gap):
    if gap <= 1:
        return 0
    return (gap + 1) // 2


def merge2(arr1, arr2, n, m):
    gap = n + m
    gap = nextGap(gap)
    while gap > 0:
        i = 0

        # comparing elements in the first array.
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]
            i += 1

        j = max(0, gap - n)

        # comparing elements in both the arrays
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        # comparing elements in second array
        if j < m:
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]
                j += 1
        gap = nextGap(gap)


# C++
"""
int nextGap(int gap) 
{ 
	if (gap <= 1) 
		return 0; 
	return (gap / 2) + (gap % 2); 
} 

// Function to merge the arrays
// arr1[], arr2[]: input arrays
// n, m: size of arrays arr1[] and arr2[] respectively
void merge(int arr1[], int arr2[], int n, int m)
{ 
	int i, j, gap = n + m; 
	
	for (gap = nextGap(gap); gap > 0; gap = nextGap(gap)) 
	{ 
	    // comparing elements in the first array. 
		for (i = 0; i + gap < n; i++) 
			if (arr1[i] > arr1[i + gap]) 
				swap(arr1[i], arr1[i + gap]); 

		// comparing elements in both arrays. 
		for (j = gap > n ? gap-n : 0 ; i < n&&j < m; i++, j++) 
			if (arr1[i] > arr2[j]) 
				swap(arr1[i], arr2[j]); 
        
        // comparing elements in the second array.
		if (j < m) 
		{ 
			
			for (j = 0; j + gap < m; j++) 
				if (arr2[j] > arr2[j + gap]) 
					swap(arr2[j], arr2[j + gap]); 
		} 
	} 
} 

"""

# Java
"""

class MergeSort
{
    public static int nextGap(int gap) { 
        if(gap <= 1) return 0; 
        return (gap / 2) + (gap % 2); 
    }
    
    public static void merge(int arr1[], int arr2[], int n, int m) {
        int i, j, gap = n + m, tmp;
        
        // comparing elements in the first array. 
        for(gap = nextGap(gap); gap > 0; gap = nextGap(gap)) {
            for(i = 0; i + gap < n; i++){
                if(arr1[i] > arr1[i + gap]){
                    tmp = arr1[i];
                    arr1[i] = arr1[i + gap];
                    arr1[i+gap] = tmp;
                }
            }
            
            // comparing elements in both arrays. 
            for(j = gap > n ? gap-n : 0 ; i < n&&j < m; i++, j++){
                if(arr1[i] > arr2[j]){
                    tmp = arr1[i];
                    arr1[i] = arr2[j];
                    arr2[j] = tmp;
                }
            }
            
            // comparing elements in the second array.
            if(j < m) {
                for (j = 0; j + gap < m; j++){
                    if(arr2[j] > arr2[j + gap]){
                        tmp = arr2[j];
                        arr2[j] = arr2[j + gap];
                        arr2[j + gap] = tmp;
                    }
                }
            }
        }
    }
}

"""