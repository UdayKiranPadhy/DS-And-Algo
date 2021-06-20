"""
832. Flipping an Image
Easy

Given an n x n binary matrix image, flip the image horizontally, then invert it, 
and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
 

Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

Example 2:

Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
 

Constraints:

n == image.length
n == image[i].length
1 <= n <= 20
images[i][j] is either 0 or 1.

"""


def flipAndInvertImage(self, A):
    for row in A:
        i, j = 0, len(row) - 1
        while i <= j:
            if row[i] == row[j]:
                row[i], row[j] = row[i] ^ 1, row[j] ^ 1
            i += 1
            j -= 1
    return A


"""
After reviewing some examples you will notice the following patterns:
1) Look at first and last value of row. If they are the same (1,1 or 0,0), 
they will be flipped in the output.
If they are different (1,0 or 0,1), they do not change. Work your way 
inward to the middle of the list
applying this rule.
2) If the row has an odd number of entries, the middle value always flips. 
For example if len(row) = 5,
then row[2] must change values.

Bitwise XOR --> 0^1 = 1, 1^1 =0

Let i be the index at the beginning of the row, and j be the index at the 
end of the row. If the the values at
these indices (row[i] and row[j]) are equal, flip their values using XOR ^. 
If they values are not equal, do nothing and move i and j closer to the middle. 
When i == j , the code still executes as it should.

Edit:
If len(A) = num_words = M and len(A[0]) = word_length = N, we iterate over 
(word_length / 2) * num_words or (N/2) * M values. Time complexity 
is O((N/2) * M), but its still just linear with the input so we can 
generalize as O(N). Space complexity is O(1).
"""
