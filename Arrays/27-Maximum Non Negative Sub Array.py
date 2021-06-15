"""
Source:- Edyst
Date:- 13/06/21

Find out the maximum sub-array of non negative numbers from an array.

The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

Example:

A : [1, 2, 5, -7, 2, 3]
The two sub-arrays are [1, 2, 5] [2, 3].
The answer is [1, 2, 5] as its sum is larger than [2, 3]
NOTE: If there is a tie, then compare with segment’s length and return segment which has maximum length

NOTE 2: If there is still a tie, then return the segment with minimum starting index


"""


class Solution:
    def maxset(self, A):
        maximum_sum = 0
        maximum_lenght = 0
        maximum_index = 0
        current_sum = 0
        current_index = 0
        current_length = 0
        change_index = True
        for i in range(len(A)):
            if A[i] >= 0:
                if change_index:
                    current_index = i
                    change_index = False
                current_sum += A[i]
                current_length += 1
            else:
                if current_sum >= maximum_sum:
                    if current_sum == maximum_sum:
                        if current_length == maximum_lenght:
                            continue
                        elif current_length > maximum_lenght:
                            maximum_lenght = current_length
                            maximum_index = current_index
                    else:
                        maximum_sum = current_sum
                        maximum_index = current_index
                        maximum_lenght = current_length
                change_index = True
                current_sum = 0
                current_length = 0
        if current_sum >= maximum_sum:
            if current_sum == maximum_sum:
                if current_length == maximum_lenght:
                    pass
                elif current_length > maximum_lenght:
                    maximum_lenght = current_length
                    maximum_index = current_index
            else:
                maximum_sum = current_sum
                maximum_index = current_index
                maximum_lenght = current_length
        return A[maximum_index:maximum_index+maximum_lenght]


string = [int(x) for x in input().strip().split(" ")]
model = Solution()
print(*model.maxset(string))
