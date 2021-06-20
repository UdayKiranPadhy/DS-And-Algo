"""
Print all the possible subarrays of the given array.

"""

n = [-1, 4, 7, 2]


def ProduceSubArrays(n: list):
    for i in range(len(n)):
        for j in range(i + 1, len(n) + 1):
            print(n[i:j])


# ProduceSubArrays(n)
"""
Find the sub array in an array which has maximum sum
"""


def kadanes(array):
    current_sum = 0
    max_sum = -99999
    for i in range(len(array)):
        current_sum += array[i]
        if current_sum < 0:
            current_sum = 0
        max_sum = max(current_sum, max_sum)
    return max_sum


# print(kadanes([-1, 4, -6, 7, 4]))


