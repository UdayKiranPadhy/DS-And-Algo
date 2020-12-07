# Quick Sort

"""
Approach:-
We take a pivot a element and keep it in its correct position .
i.e, The numbers to the left must be less than pivot and number to right must be greater than the pivot

Note:- the numbers to the left need not to be sorted we just need to fix the position of pivot

"""


def quick_sort(l):
    lenght = len(l)
    if lenght <= 1:
        return l
    else:
        pivot = l[lenght // 2]
        del l[lenght // 2]
    items_smaller = []
    items_greater = []
    for i in l:
        if i > pivot:
            items_greater.append(i)
        else:
            items_smaller.append(i)
    return quick_sort(items_smaller) + [pivot] + quick_sort(items_greater)


# As we can see that more space is being used in this method .
# We can optmize it by this following method
def quicksort(start, end, A):
    if start < end:
        p = position(start, end, A)
        quicksort(start, p - 1, A)
        quicksort(p + 1, end, A)
        print(A)


def position(start, end, A):
    if start < end:
        pivot = A[end]
        i = start
        j = end - 1
        while i < 1:
            while A[i] < pivot and i < end:
                i = i + 1
            while A[j] < pivot and j >= start:
                j = j - 1
            if i < j:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
            temp = A[i]
            A[i] = A[end]
            A[end] = temp
        return i


A = [8, 4, 1, 5, 3, 10, 7, 6]
print(quicksort(0, len(A) - 1, A))

# l = list(map(int, input().split()))
# print(*quick_sort(l))
