"""
Count Inversions 
Easy 
Given an array of integers. Find the Inversion Count in the array. 

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 

Example 1:

Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 
has three inversions (2, 1), (4, 1), (4, 3).
Example 2:

Input: N = 5
arr[] = {2, 3, 4, 5, 6}
Output: 0
Explanation: As the sequence is already 
sorted so there is no inversion count.
Example 3:

Input: N = 3, arr[] = {10, 10, 10}
Output: 0
Explanation: As all the elements of array 
are same, so there is no inversion count.
Your Task:
You don't need to read input or print anything. Your task is to complete the function inversionCount() which takes the array arr[] and the size of the array as inputs and returns the inversion count of the given array.

Expected Time Complexity: O(NLogN).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 5*105
1 ≤ arr[i] ≤ 1018

Company Tags
 Adobe Amazon BankBazaar Flipkart Microsoft Myntra
Topic Tags
 Arrays Sorting Divide and Conquer
"""

# HInt 1
"""
A naive solution to this would be to use 2 nested for-loops and for every index i, find the count of elements greater than arr[i] to the right of it. Finally, return the sum of such counts for every value of 0 <= i < n. 

But the time complexity of this will be O(n2). Can we make it better? 
"""

# Hint 2
"""
We basically need to make the comparisons in the existing array and while doing any comparison, we need to know that how would the two numbers being compared would be ordered in the sorted version of this array.
So, how about running a sorting algorithm itself?
The algorithms like Bubble Sort, Insertion Sort and Selection sort are O(n2). We can achieve this complexity even via the naive approach discussed in the previous hint, so no use of it.

What about getting to this via merge sort?
"""

# Hint 3
"""
Use Merge sort algorithm, and sort the array.
In merge function for merge sort, while comparing the elements, if element in right array is smaller, then it is an inversion (Why..??)
This means that this smaller element in the original array, is behind larger elements. So add the number of larger elements or elements left in the left-array, to the value of counter.
This process is repeated again and again for complete Merge Sort
Finally output counter variable. This is the answer.
"""


# Counting Inversions but not n^2 it is need to done with nlogn complexity so its a modified merge sort


inversion_count = 0  # global variable to count total inversions


def inversionCount(a, n):
    global inversion_count
    inversion_count = 0
    merge_sort(a, 0, n - 1)
    return inversion_count


# merger of two halves .. counting inversion at each step
def merge(a, start, mid, end):
    global inversion_count
    temp = [0 for i in range(end - start + 1)]
    i, j, k = start, mid + 1, 0  # indexes of left,right and temp arrays

    # merge while conditions are valid
    while i <= mid and j <= end:

        # compare the elements and merge
        if a[i] <= a[j]:
            temp[k] = a[i]
            k += 1
            i += 1
        else:
            temp[k] = a[j]
            k += 1
            j += 1
            inversion_count += (
                mid - i + 1
            )  # inversion occurs here as right moved ahead of left

    # storing the rest elements
    while i <= mid:
        temp[k] = a[i]
        k += 1
        i += 1

    # storing the rest elements
    while j <= end:
        temp[k] = a[j]
        k += 1
        j += 1

    for i in range(start, end + 1):
        a[i] = temp[i - start]


# merge utility
def merge_sort(a, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(a, start, mid)
        merge_sort(a, mid + 1, end)
        merge(a, start, mid, end)

# C++
"""
long long my_counter = 0;

// Function to merge two parts of array
// p: initial point in the array, say left index
// q: mid point
// r: higher range
void merge(long long a[], long long p, long long q, long long r){
    long long l = q-p+1;
    long long a1[l];

    long long l2 = r-q;
    
    long long a2[l2];
    
    // storing elements on left half from a to a1
    for(long long i = 0;i<l;i++){
        a1[i] = a[i+p];
    }
    
    // storing elements on right half from a to a2
    for(long long i = 0;i<l2;i++){
        a2[i] = a[q+i+1];
    }
    
    long long left = 0, right = 0, k = p;
    
    // merge while indexes are valid
    while(left < l && right < l2)
    {
        // comparing element of a1 and a2
        // and accordingly storing in a
        if(a1[left] <= a2[right]){
            a[k] = a1[left];
            left++;
        }
        else{
            a[k] = a2[right];
            right++;
            
            // add the inversions that cross between 
            // the first half and second half
            my_counter += (l-left); // Increementing counter
        }
        k++;
    }
    
    // store the rest elements
    while(left < l){
        a[k++] = a1[left++];
      
    }
    
    // store the rest elements 
    while(right < l2){
        
        a[k++] = a2[right++];
    }
}

// Function to mergesort a[], which use 
// divide and conquer for left and right mergesort
// operation
void mergeSort(long long a[], long long p, long long r)
{
    
    if(p < r)
    {
        // mid
        long long q = (p+r)/2;
        
        // calling for left half
        mergeSort(a, p, q);
        
        // calling for right half
        mergeSort(a, q+1, r);
        
        // after sorting, need to call merge funtion
        merge(a, p, q, r);
    }
}

// base function which calls the other utility function
// to find the number of inversions
long long int inversionCount(long long arr[],long long N)
{
    mergeSort(arr,0,N-1);
    long long int res = my_counter;
    my_counter = 0;
    return res;
}
"""