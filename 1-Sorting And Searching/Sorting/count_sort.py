"""
Procedure :- 
1) Find the count of every distinct element in the array
2) Calculate the position of each element in the sorted array

"""

# Example
"""
Example Array
1 , 3 , 2 , 3 , 4 , 1 , 6 , 4 , 4 , 3

Now we need to make a count array 
the Size of count array will be the maximum element of the Array

Count Array  0  2  1  3  2  0  1
Index        0  1  2  3  4  5  6

index 1 => element 1 is stored in Array 2 times so count_Array[1]=2
index 6 => element 6 is stored in Array 1 time so count_Array[6] = 1

