"""
Next Larger Element (A)
Given an array, find the Next greater element for every element.

The Next greater Element for an element x is the first greater element on the right side of x in array.

Elements for which no greater element exist, consider next greater element as -1.

Example :
Input :
A : [4, 5, 2, 25]
Output :
   [5, 25, 25, -1]
"""


class Solution:
    def nextGreaterElement(self, arr):
        l = []
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] < A[j]:
                    l.append(A[j])
                    break
            else:
                l.append(-1)

        return l


class Solution:
    def nextGreaterElement(self, arr):
        stack = []
        n = len(A)
        output = [-1 for i in range(n)]
        for i in range(n):
            if len(stack) == 0:
                stack.append(arr[i])
                continue
            else:
                if stack[-1] > arr[i]:
                    stack.append(arr[i])
                    continue
                else:
                    while stack and stack[-1] < arr[i]:
                        output[arr.index(stack.pop(-1))] = arr[i]
                    stack.append(arr[i])
        return output
