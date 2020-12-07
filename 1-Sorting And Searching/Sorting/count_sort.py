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

Now we get the position array

position array 0  2  3  6  8  8  9
               0  1  2  3  4  5  6
        
Keep adding the previous got sum 

Now make a array of size of the give array and start traversing the given array from end
the elemnt is 3 ,we will check the position of the element 3 in the position array and then place it in the new array
after placeing it we decrease the count in position array

       _ _ _ _ _ _ _ _  new array
       _ _ _ _ 3 _ _ _  after placing the element in its position
       0  2  3  5  8  8  9 updating position array after placing the element in the new array

       next element 4
       _ _ _ _ 3 _ 4 _
       0  2  3  5  7  8  9
"""

A = [1, 3, 1, 2, 3, 4, 1, 6, 4, 4, 3]

count = [0 for i in range(max(A) + 1)]
position = [0 for i in range(len(count))]
output_array = [0 for i in range(len(A))]

for i in range(len(count)):
    count[i] = A.count(i)
for i in range(len(position)):
    if i == 0:
        position[i] = count[i]
    else:
        position[i] = position[i - 1] + count[i]
for i in range(len(A) - 1, -1, -1):
    pos = A[i]
    position[pos] -= 1
    output_array[position[pos]] = A[i]
print(output_array)