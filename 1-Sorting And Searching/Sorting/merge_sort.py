"""
Pre-requiristics :-

Sort two different arrays in one, Given the two arrays are already sorted. 
Input :-
A= [3,5,6,7,8,9]
B=[1,2,3,4,5,8]
Output :-
[1,2,3,3,4,5,5,6,7,8,8,9]
"""


def merge(A, B):
    i = 0
    j = 0
    c = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            c.append(A[i])
            i += 1
        else:
            c.append(B[j])
            j += 1

    # If in case j reaches len(B) and i didn't complete its complete List
    for k in range(i, len(A)):
        c.append(A[k])

    for k in range(j, len(B)):
        c.append(B[k])

    return c


# A = [1, 2, 5, 6, 8, 10, 15]
# B = [8, 15, 19, 22, 25, 88, 92, 98]
# print(A)
# print(B)
# print(merge(A, B))


"""
Now comes the merge sort, inmerge sort we divide the array into multiple parts till we get single element .
And then we merge the individual single elements into group once.
"""

# Some thing Like this
"""
def merge_sort(start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid - 1)
        merge_sort(mid, end)
        merge(l[:mid], l[mid:])


l = [5, 4, 5, 4, 8, 6, 2, 1, 0, 4, 5]
merge_sort(0, len(l))
print(l)
"""


def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        merge_sort(left)
        merge_sort(right)

        # Merge the lists now
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
                k += 1
            else:
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


l = list(map(int, input().split()))
merge_sort(l)
print(*l)

"""
Time Complexity : nlogn
Space Complexity : nlogn

n if for that merge function and logn is the number of times 
"""