"""

Given an array of integers, find the closest (not considering distance, but value) 
smaller on left of every element. If an element has no smaller on the left side, print -1.

arr[] : 4   5   2   10   8
output: -1  4   -1   2    2

"""


def NSL(arr):
    output = []
    stack = []
    for i in range(len(arr)):
        if len(stack) == 0:
            output.append(-1)
        elif len(stack) > 0 and stack[-1] < arr[i]:
            output.append(stack[-1])
        elif len(stack) > 0 and stack[-1] >= arr[i]:
            while len(stack) > 0 and stack[-1] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                output.append(-1)
            else:
                output.append(stack[-1])
        stack.append(arr[i])
    return output


arr = [4, 5, 2, 10, 8]
print(arr)
print(NSL(arr))
