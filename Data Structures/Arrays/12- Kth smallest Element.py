"""

Kth smallest element 

Given an array arr[] and a number K where K is smaller than size of array, 
the task is to find the Kth smallest element in the given array. It is 
given that all array elements are distinct.

Example 1:
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given 
array is 7.

Example 2:
Input:
N = 5
arr[] = 7 10 4 20 15
K = 4
Output : 15
Explanation :
4th smallest element in the given 
array is 15.

Your Task:
You don't have to read input or print anything. Your task is to complete the function 
kthSmallest() which takes the array, it's size and an integer k as input and returns 
the kth smallest element.
 
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^5
1 <= arr[i] <= 10^5
1 <= K <= N
 
Company Tags
 ABCO Accolite Amazon Cisco Hike Microsoft Snapdeal VMWare
Topic Tags
 Arrays Searching Sorting
"""
# There are four solutions for it.
# 1) Sort the array and return the 4th number
# time complexity is nlogn

# 2)Take a auxilary array of size k and append elements using insertion sort , at the
# end we get the k smallest elements.
# time complexity is n.K

# 3)Using Heap sort :
# Take a heap of size k and keep updating its head until the list ends and then return the 
# head of the heap.
# time complexity nlogk

# 4)Using partation of quick sort at k index.

# Solution 1
def kthSmallest(arr, k):
    arr.sort()
    # print(arr)
    return arr[k - 1]


# print(kthSmallest([5, 5, 6, 4, 1, 8, 32, 2, 4, 0, 9], 5))

# Solution 2
def insertsort(element, arr, k):
    if arr[k - 1] <= element:
        return
    arr.pop()
    for i in range(len(arr)):
        if arr[i] >= element:
            arr.insert(i, element)
            break
    else:
        arr.append(element)


def smallestelement(arr, k):
    l = arr[:k]
    l.sort()
    for i in range(k, len(arr)):
        insertsort(arr[i], l, k)
    print(l)
    return l[k - 1]


print(smallestelement([5, 8, 9, 3, 1, 4, 5, 6, 7, 5, 3, 4, 4], 5))
