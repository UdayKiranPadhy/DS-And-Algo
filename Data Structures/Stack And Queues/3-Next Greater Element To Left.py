"""
Given an array of integers, find the closest (not considering distance, but value) 
greater on left of every element. If an element has no greater on the left side, print -1.

arr[] : 1   3   2   4
output: -1  -1  3   -1
"""

# Solution
"""
Change : 
1) Left to Right
2) No Reversal Needed
"""


def NGEL(arr):
    output = []
    stack = []
    for i in range(len(arr)):
        if len(stack) == 0:
            output.append(-1)
        elif len(stack) > 0 and stack[-1] > arr[i]:
            output.append(stack[-1])
        elif len(stack) > 0 and stack[-1] <= arr[i]:
            while len(stack) > 0 and stack[-1] <= arr[i]:
                stack.pop()
            if len(stack) == 0:
                output.append(-1)
            else:
                output.append(stack[-1])
        stack.append(arr[i])
    return output


print(NGEL([1, 3, 2, 4]))
