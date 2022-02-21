"""
versions in an array | Set 1 (Using Merge Sort)
 
Inversion Count for an array indicates – how far (or close) the array is from being 
sorted. If array is already sorted then inversion count is 0. If array is sorted in 
reverse order that inversion count is the maximum. 
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] 
and i < j 

Example: 

Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).


Input: arr[] = {3, 1, 2}
Output: 2

Explanation: Given array has two inversions:
(3, 1), (3, 2) 

"""
# Method-1
A = [2, 1, 3, 1, 2]
count = 0
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] > A[j]:
            count += 1
# print(count)

"""
Time Complexity 
0->n
1->n-1
2->n-2
.
.
n->0

Number of times the inner most loops runs n + n- 1 + n-2 + ... .+n - n
n*(n-1)/2 ~= n^2
"""

# Method 2
"""
Modified MergeSort
"""


def MergeSort(l):
    count = 0
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        count += MergeSort(left)
        count += MergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                l[k] = left[i]
                i += 1
                k += 1
            else:
                count += len(left) - i
                l[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1
    return count


print(MergeSort(A))
print(A)
